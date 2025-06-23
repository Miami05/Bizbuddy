from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(2))


class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    category = db.Column(db.String(50))
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"))


class ChecklistStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    step_number = db.Column(db.Integer)
    content = db.Column(db.String(255))
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"))
