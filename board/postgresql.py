import psycopg2
import click
from flask import current_app, g
from psycopg2.extras import RealDictCursor


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@click.command("init-db-pgsql")
def init_db_command():
    db = get_db()

    with db.cursor() as cursor:
        cursor.execute(open("./board/schema-postgres.sql", "r").read())
        db.commit()
        cursor.close()

    click.echo("You successfully initialized the database!")


def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(
            host=current_app.config["DB_HOST"],
            database=current_app.config["DB_NAME"],
            user=current_app.config["DB_USERNAME"],
            password=current_app.config["DB_PASSWORD"],
            cursor_factory=RealDictCursor)
    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()
