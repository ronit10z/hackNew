from flask import request, render_template

from app import app


@app.route("/")
def index():
    return "Homepage :  method use - %s" % request.method


@app.route("/bacon", methods=["GET", "POST"])
def bacon():
    if request.method == "POST":
        return "you are using POST"
    else:
        return "You are using GET"


@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html")


@app.route("/id/<int:id>")
def getId(id):
    assert isinstance(id, int)
    return "The id is %d" % id
