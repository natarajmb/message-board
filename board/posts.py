from flask import Blueprint, render_template, redirect, request, url_for

from board.postgresql import get_db

bp = Blueprint("posts", __name__)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO post (author,message) VALUES (%s,%s)", (author, message)
            )
            db.commit()
            cursor.close()
            return redirect(url_for("posts.posts"))

    return render_template("posts/create.html")


@bp.route("/posts")
def posts():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT author, message, created FROM post ORDER BY created DESC"
    )
    posts = cursor.fetchall()
    db.commit()
    cursor.close()
    return render_template("posts/posts.html", posts=posts)
