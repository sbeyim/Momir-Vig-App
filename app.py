from flask import Flask, render_template, abort
import ScryfallRequest

app = Flask(__name__)

Missing_Mana_Values = {14}
Mana_Values = [mv for mv in range(0, 17) if mv not in Missing_Mana_Values]



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


if __name__ == "__main__":
    app.run(debug=False)