import os

from flask import Flask

# Set up paths
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize and configure app
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
