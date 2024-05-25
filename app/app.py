from flask import Flask, render_template, request, redirect
from jinja2 import Environment, PackageLoader, select_autoescape

from app.src.datastructure.TreeManager import generate_tree
from app.src.datastructure.tree.Tree import Tree

env = Environment(
    loader=PackageLoader(__name__),
    autoescape=select_autoescape()
)

app = Flask(__name__)


class Controller:
    def __init__(self):
        self.tree = None
        self.initiated_game = False

    def initialize(self, difficulty):
        if not self.initiated_game:
            self.tree = generate_tree(difficulty.value)
            self.initiated_game = True

    def end(self):
        self.tree = None
        self.initiated_game = False


controller = Controller()


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


@app.route("/game/init/<difficulty>")
def init(difficulty):
    controller.initialize(difficulty)
    return game()


@app.route("/game/end")
def end():
    controller.end()
    return index()


@app.route("/game")
def game():
    if not controller.initiated_game:
        return index()
    template = env.get_template("game.html")
    return template.render(
        game_state=controller.tree.root.state,
        winning_state=controller.tree.is_winning()
    )





if __name__ == "__main__":
    app.run(debug=True)