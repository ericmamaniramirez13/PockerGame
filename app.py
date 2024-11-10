from flask import Flask, render_template
from src.game.deck import Deck

app = Flask(__name__, template_folder="src/templates")

@app.route("/")
def index():
    deck = Deck()
    hand = deck.draw(5)
    return render_template("index.html", hand=hand)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=3000, debug = True)