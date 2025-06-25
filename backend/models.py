from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

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


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class ChecklistProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    step_id = db.Column(db.Integer, db.ForeignKey("checklist_step.id"))
    completed = db.Column(db.Boolean, default=False)


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tip_id = db.Column(db.Integer, db.ForeignKey("tip.id"))
