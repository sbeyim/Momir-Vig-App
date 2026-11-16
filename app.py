from flask import Flask, render_template, abort
import ScryfallRequest
import re
from markupsafe import Markup, escape

app = Flask(__name__)

Missing_Mana_Values = {14}
Mana_Values = [mv for mv in range(0, 17) if mv not in Missing_Mana_Values]

SYMBOL_PATTERN = re.compile(r"\{([A-Z0-9/]+)\}")


@app.template_filter("mana")
def mana_filter(text):
    if not text:
        return ""

    safe_text = str(escape(text))   # neutralize any HTML in the data first

    def to_image(match):
        code = match.group(1)               # e.g. "W", "2", "W/U", "T"
        file_name = code.replace("/", "")   # "W/U" -> "WU"
        return (
            f'<img class="mana-symbol" '
            f'src="https://svgs.scryfall.io/card-symbols/{file_name}.svg" '
            f'alt="{{{code}}}">'
        )

    return Markup(SYMBOL_PATTERN.sub(to_image, safe_text))

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/play")
def play():
    return render_template("play.html", mana_values=Mana_Values)


@app.route("/creature/<int:mana_value>")
def creature(mana_value):
    if mana_value not in Mana_Values:
        abort(404)
    card = ScryfallRequest.Get_Random_Creature(mana_value)
    return render_template("creature.html", mana_value=mana_value, card=card)

@app.route("/rules")
def rules():
    return render_template("rules.html")


if __name__ == "__main__":
    app.run(debug=False)