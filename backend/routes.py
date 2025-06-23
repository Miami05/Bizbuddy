from flask import Blueprint, render_template, request, jsonify
from models import Country, Tip, ChecklistStep

main = Blueprint("main", __name__)


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
def get_checklist(country_id):
    step = (
        ChecklistStep.query.filter_by(country_id=country_id)
        .order_by(ChecklistStep.step_number)
        .all()
    )
    return jsonify(
        [{"id": s.id, "step_number": s.step_number, "content": s.content} for s in step]
    )
