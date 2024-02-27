import os
import logging
import sys
from flask import Flask
from dotenv import load_dotenv
from board import pages, posts, postgresql
from pyservicebinding import binding

# check if running on k8s with service bindings
try:
    logging.info("Loading SERVICE_BINDING_ROOT")
    sb = binding.ServiceBinding()
    bl = sb.bindings("postgresql")
    if len(bl) > 1:
        logging.error("expected 1 binding of type 'postgresql': got %d", len(bl))
        sys.exit(3)
    b = bl[0]
    os.environ["FLASK_DB_HOST"] = b["host"]
    os.environ["FLASK_DB_NAME"] = b["database"]
    os.environ["FLASK_DB_USERNAME"] = b["username"]
    os.environ["FLASK_DB_PASSWORD"] = b["password"]

except binding.ServiceBindingRootMissingError as msg:
    # log the error message if not
    logging.error("SERVICE_BINDING_ROOT env var not set")
    # try loading .env file from local
    logging.info("Loading .env")
    if not load_dotenv():
        logging.error(".env not found")
        logging.error("No database configured... exiting")
        sys.exit(3)


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    postgresql.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)

    logging.info("Current Environment: ", os.getenv('ENVIRONMENT'))
    logging.info("Using Database: ", os.getenv('DB_NAME'))

    return app
