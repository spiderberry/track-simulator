from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("blog", __name__)

@bp.route("/")
def index():
    db = get_db()
    posts = db.execute(
        "SELECT p.id, title, body, created, author_id, username"
        " FROM post p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()

    return render_template("blog/index.html", posts = posts)

@bp.route("/create", methods = ("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, body, author_id)"
                " VALUES (?, ?, ?)",
                (title, body, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("blog.index"))
        
    return render_template("blog/create.html")

def get_post(id, check_author = True):
    post = get_db().execute(
        "SELECT p.id, title, body, created, author_id, username"
        " FROM post p JOIN user U ON p.author_id = u.id"
        " WHERE p.id = ?",
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post

@bp.route("/<int:id>/update", methods = ("GET", "POST"))
@login_required
def update(id):
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE post SET title = ?, body = ?"
                "WHERE id = ?",
                (title, body, id)
            )
            db.commit()
            return redirect(url_for("blog.index"))
        
    return render_template("blog/update.html", post = post)
        
@bp.route("/<int:id>/delete", methods = ("POST",))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("blog.index"))

@bp.route("/create_athlete", methods = ("GET", "POST"))
@login_required
def create_athlete():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        age = request.form["age"]
        acceleration = request.form["acceleration"]
        endurance = request.form["endurance"]
        form = request.form["form"]
        mental = request.form["mental"]
        start = request.form["start"]
        speed = request.form["speed"]
        error = None

        if not first_name:
            error = "First name is required."

        elif not last_name:
            error = "Last name is required."

        elif not age:
            error = "Age is required."

        elif not acceleration:
            error = "Acceleration is required."

        elif not endurance:
            error = "Endurance is required."

        elif not form:
            error = "Form is required."

        elif not mental:
            error = "Mental is required."

        elif not speed:
            error = "Speed is required."
            
        elif not start:
            error = "Start is required."

        elif error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            user_id = g.user["id"]
            athlete_id = cursor.execute(
                "SELECT athlete_id FROM user WHERE id = ?", (user_id,)
            ).fetchone()[0]
            cursor.execute(
                "UPDATE Athletes "
                 "SET first_name = ?, "
                    "last_name = ?, "
                    "age = ?, "
                    "acceleration = ?, "
                    "endurance = ?, "
                    "form = ?, "
                    "mental = ?, "
                    "speed = ?, "
                    "start = ? "
                "WHERE id = ?",
                (first_name, last_name, age, acceleration, endurance, form, mental, speed, start, athlete_id),
            )
            db.commit()
            return redirect(url_for("blog.index"))
        
    return render_template("blog/create_athlete.html")