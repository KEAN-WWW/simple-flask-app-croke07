from flask import Flask

# package-level Flask app object used by routes and tests
app = Flask(__name__)

# import routes so @app.route handlers register
from . import app as _routes  # noqa: F401

