from flask import Flask, render_template, request, redirect
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader(__name__),
    autoescape=select_autoescape()
)

app = Flask(__name__)


@app.route("/")
def index():
    template = env.get_template("index.html")
    return template.render()


@app.route("/rules")
def rules():
    template = env.get_template("rules.html")
    return template.render()


@app.route("/examples")
def examples():
    template = env.get_template("examples.html")
    return template.render()


@app.route("/history")
def history():
    template = env.get_template("history.html")
    return template.render()

@app.route("/game")
def game():
    template = env.get_template("game.html")
    return template.render()


if __name__ == "__main__":
    app.run(debug=True)