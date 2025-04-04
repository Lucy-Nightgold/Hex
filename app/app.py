from flask import Flask, Response, redirect
from jinja2 import Environment, PackageLoader, select_autoescape

from src.Difficulty import Difficulty, get_difficulty_by_number
from src.Game import Game

env = Environment(
    loader=PackageLoader(__name__),
    autoescape=select_autoescape()
)

app = Flask(__name__)


class Controller:
    def __init__(self):
        self.game = None
        self.initiated_game = False

    def initialize(self, difficulty):
        if not self.initiated_game:
            self.game = Game(difficulty)
            self.initiated_game = True

    def end(self):
        self.game = None
        self.initiated_game = False


controller = Controller()


@app.route("/")
def index():
    template = env.get_template("index.html.j2")
    return template.render()


@app.route("/examples")
def examples():
    template = env.get_template("examples.html.j2")
    return template.render()


@app.route("/historyAndRules")
def history():
    template = env.get_template("historyAndRules.html.j2")
    return template.render()


@app.route("/game/init/<difficulty>")
def init(difficulty):
    controller.initialize(get_difficulty_by_number(difficulty))
    return redirect("/game")


@app.route("/game/end")
def end():
    controller.end()
    return redirect("/")


@app.route("/game/restart/<difficulty>")
def restart(difficulty):
    controller.end()
    controller.initialize(get_difficulty_by_number(difficulty))
    return redirect("/game")


@app.route("/game")
def game():
    if not controller.initiated_game:
        return redirect("/")
    template = env.get_template("game.html.j2")
    return render_game()


@app.route("/game/play/<case>")
def play(case):
    if not controller.initiated_game:
        return redirect("/")
    case = int(case)
    try:
        controller.game.play_turn(case)
    except Exception as e:
        return Response(repr(e), 403)
    else:
        return render_game()


def render_game():
    template = env.get_template("game.html.j2")
    return template.render(
        game_state=controller.game.tree.root.state,
        winning_state=controller.game.tree.is_winning().value
    )


if __name__ == "__main__":
    app.run(debug=True)
