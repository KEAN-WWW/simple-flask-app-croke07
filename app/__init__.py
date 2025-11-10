from flask import Flask

app = Flask(__name__)
from .app import *  # noqa: F401,F403  (registers routes)
