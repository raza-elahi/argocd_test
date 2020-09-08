"""
Simple app for testing argocd.
"""

from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
