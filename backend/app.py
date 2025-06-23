from flask import Flask
from models import db
from routes import main
import os

static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))
app = Flask(__name__, static_folder=static_dir)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
