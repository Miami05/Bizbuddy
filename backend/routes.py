from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from models import db, Country, Tip, ChecklistStep, ChecklistProgress, Bookmark
from flask_login import login_required, current_user
import cohere
import os
from dotenv import load_dotenv

load_dotenv()
main = Blueprint("main", __name__)
co = cohere.Client(os.getenv("COHERE_API_KEY"))


# --- Login redirect at root ---
@main.route("/")
def index():
    return redirect(url_for("auth.login"))


# --- Homepage: Searchable country selector ---
@main.route("/home")
def home():
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


# --- AI suggestions ---
@main.route("/api/suggest", methods=["POST"])
def suggest_ai():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON provided"}), 400

    country = data.get("country")
    keyword = data.get("keyword")

    # Enhanced prompt with better structure and instructions
    prompt = f"""
You are an expert startup consultant specializing in {country} business regulations and startup guidance.

A startup founder in {country} needs specific guidance on: "{keyword}"

Please provide a comprehensive, actionable guide with the following structure:

ACTIONABLE STEPS (4-6 steps):
Each step should be:
- Specific and actionable
- Include estimated timeframes where relevant
- Mention specific forms, websites, or authorities
- Include approximate costs if applicable

NETWORKING & RESOURCES (3-5 opportunities):
- List specific local programs, accelerators, networking events, or government initiatives in {country}
- Include organization names and brief descriptions of what they offer
- Provide website URLs or contact information where available
- Mention any application deadlines or requirements

USEFUL LINKS & RESOURCES:
- Government websites for official registration/licensing
- Key regulatory bodies or departments
- Funding databases or grant portals specific to {country}
- Professional associations or industry groups

CONCLUSION:
- One concise sentence summarizing the key takeaway

Format your response clearly with proper spacing and structure. Be specific about {country} regulations and requirements. Focus on practical, implementable advice rather than general guidance. Include actual website URLs and contact details wherever possible.
"""

    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=1000,  # Increased for more detailed responses
            temperature=0.5,  # Slightly lower for more consistent, factual responses
            stop_sequences=["\n\n---"],  # Optional: to prevent overly long responses
        )
        suggestion = response.generations[0].text.strip()
        return jsonify({"suggestion": suggestion})

    except Exception as e:
        return jsonify(
            {"error": "AI service temporarily unavailable", "details": str(e)}
        ), 500
