from flask import Flask

# Flask application object that tests will import
app = Flask(__name__)

# Import routes so the @app.route handlers get registered
from . import app as _routes  # noqa: F401
