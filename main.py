from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_KEY")


@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


@app.route("/resume", methods=["GET"])
def resume_page():
    return render_template("resume.html")


@app.route("/projects", methods=["GET"])
def projects_page():
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)
