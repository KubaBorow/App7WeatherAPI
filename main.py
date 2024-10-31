from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


@app.route("/contact-us/")
def contact():
    return render_template("contact.html")

# Jeśli chcemy uruchomić kilka aplikacji na raz musimy wyszczerólnić port na którym działają, np port = 5001,
# domyslnie jest ustawiony port 5000
if __name__ == "__main__":
    app.run(debug=True)
