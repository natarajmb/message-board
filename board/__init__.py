import os
from flask import Flask
from dotenv import load_dotenv
from board import pages, posts, postgresql

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    postgresql.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DB_NAME')}")
    return app
