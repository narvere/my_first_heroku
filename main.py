# app/main.py

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    app.run()
