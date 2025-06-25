from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.sql.functions import user
from models import db, User, Bookmark, Tip, Country, ChecklistProgress, ChecklistStep
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


# --- Login Page ---
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not email or not password:
            flash("Please fill in all fields")
            return redirect(url_for("auth.login"))
        user = User.query.filter_by(email=email).first()
        if (
            user
            and user.password_hash is not None
            and check_password_hash(user.password_hash, password)
        ):
            login_user(user)
            flash("Login successful!")
            return redirect(url_for("main.index"))
        else:
            flash("Invalid email or password")
            return redirect(url_for("auth.login"))
    return render_template("login.html")


# --- Register Page ---
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if not ([username, email, password, confirm_password]):
            flash("Please fill in all fields")
            return redirect(url_for("auth.register"))
        if password != confirm_password:
            flash("Password do not match")
            return redirect(url_for("auth.register"))
        if User.query.filter_by(user=username).first():
            flash("Email already registered")
            return redirect(url_for("auth.register"))
        if User.query.filter_by(user=username).first():
            flash("Username already token")
            return redirect(url_for("auth.register"))
        new_user = User()
        new_user.user = username
        new_user.email = email
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! Please login.")
        return redirect(url_for("auth.login"))
    return render_template("login.html")


# --- Logout ---
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for("main.index"))


# --- User Profile ---
@auth.route("/profile")
@login_required
def profile():
    bookmarks = (
        db.session.query(Bookmark, Tip, Country)
        .join(Tip, Bookmark.tip_id == Tip.id)
        .join(Country, Tip.country_id == Country.id)
        .filter(Bookmark.user_id == current_user.id)
        .all()
    )
