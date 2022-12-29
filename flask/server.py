from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    today = datetime.date.today()
    year = today.year
    random_number = random.randint(1, 10)
    return render_template("index.html", random_number=random_number, year=year)


if __name__ == "__main__":
    app.run(debug=True)
