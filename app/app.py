from flask import render_template
from . import app  # import the Flask app object

@app.route("/")
def index():
    return "Hello CPS3500!"

@app.route("/new_page")
def new_page():
    return "This is a New Page!"

@app.route("/user/<username>")
def user(username: str):
    # If the username is 'jack' (case-insensitive), show the CAPITALIZED name.
    # Otherwise show 'Anonymous!'
    name = username.upper() if username.lower() == "jack" else "Anonymous!"
    return render_template("greet.html", name=name)
