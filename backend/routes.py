from flask import Blueprint, render_template, request, jsonify
from models import db, Country, Tip, ChecklistStep, ChecklistProgress, Bookmark
from flask_login import login_required, current_user
import cohere
import os
from dotenv import load_dotenv

load_dotenv()
main = Blueprint("main", __name__)
co = cohere.Client(os.getenv("COHERE_API_KEY"))


# --- Homepage: Searchable country selector ---
@main.route("/")
def index():
    return render_template("index.html")


# --- Country details page ---
@main.route("/country/<int:country_id>")
def country_detail(country_id):
    country = Country.query.get_or_404(country_id)
    return render_template("country_detail.html", country=country)


# --- API: Country search for typehead dropdown ---
@main.route("/api/countries")
def api_countries():
    query = request.args.get("q", "").lower()
    countries = Country.query.all()
    result = [
        {
            "id": c.id,
            "name": c.name,
            "flag": f"https://flagcdn.com/w40/{c.code.lower()}.png",
        }
        for c in countries
        if query in c.name.lower()
    ]
    return jsonify(result)


# --- API: Get tips by country ---
@main.route("/api/tips/<int:country_id>")
def get_tips(country_id):
    tips = Tip.query.filter_by(country_id=country_id).all()
    return jsonify(
        [{"id": t.id, "content": t.content, "category": t.category} for t in tips]
    )


# --- API: Get checklist by country ---
@main.route("/api/checklist/<int:country_id>")
def get_checklist(country_id):
    step = (
        ChecklistStep.query.filter_by(country_id=country_id)
        .order_by(ChecklistStep.step_number)
        .all()
    )
    return jsonify(
        [{"id": s.id, "step_number": s.step_number, "content": s.content} for s in step]
    )


# --- API: Save checklist progress ---
@main.route("/api/checklist-progress", methods=["POST"])
@login_required
def save_progress():
    data = request.get_json()
    step_id = data.get("step_id")
    completed = data.get("completed")
    if step_id is None or completed is None:
        return jsonify(
            {"status": "error", "message": "Missing step_id or completed value"}
        ), 400
    progress = ChecklistProgress.query.filter_by(
        user_id=current_user.id, step_id=step_id
    ).first()
    if not progress:
        progress = ChecklistProgress()
        progress.user_id = current_user.id
        progress.step_id = step_id
        db.session.add(progress)
    progress.completed = completed
    db.session.commit()
    return jsonify({"status": "ok"})


# --- API: Bookmark Tip ---
@main.route("/api/bookmark", methods=["POST"])
@login_required
def bookmark_tip():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    tip_id = data.get("tip_id")
    if not tip_id:
        return jsonify({"error": "tip_id is required"}), 400
    existing_bookmark = Bookmark.query.filter_by(
        user_id=current_user.id, tip_id=tip_id
    ).first()
    if existing_bookmark:
        return jsonify({"message": "Already bookmarked"}), 200
    bookmark = Bookmark()
    bookmark.user_id = current_user.id
    bookmark.tip_id = tip_id
    db.session.add(bookmark)
    db.session.commit()
    return jsonify({"message": "Bookmark added successfully"}), 201


# --- API: Cohere AI suggestions ---
@main.route("/api/suggest", methods=["POST"])
def suggest_ai():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON provided"}), 400
    country = data.get("country")
    keyword = data.get("keyword")
    prompt = f"""
You are a startup assistand

The user is in {country} and wants to know how to handle '{keyword}'.
Give a clear step-by-step startup guide (4–6 steps), each step with optional links.
Finish with one local event or program to join, and a one-line conclusion.

Format it in a numbered list.
	"""
    response = co.generate(
        model="command", prompt=prompt, max_tokens=300, temperature=0.7
    )
    suggestion = response.generations[0].text.strip()
    return jsonify({"suggestion": suggestion})
