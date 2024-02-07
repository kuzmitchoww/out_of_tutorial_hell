import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

SECRET_KEY = os.urandom(16)
app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html",
                           title="My Portfolio")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html",
                           title="My Prices")


@app.route("/contact")
def contact():
    return render_template("contact.html",
                           title="Contact Me")


if __name__ == "__main__":
    app.run(debug=True)
