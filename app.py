import os
from flask import Flask, render_template, request, redirect, url_for

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

current_user = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    global current_user

    if request.method == "POST":

        username = request.form.get("username")

        current_user = username

        return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    global current_user

    if not current_user:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=current_user
    )

@app.route("/logout")
def logout():

    global current_user

    current_user = None

    return redirect(url_for("home"))

@app.route("/atencion")
def atencion():
    return render_template("atencion.html")

@app.route("/automatizacion")
def automatizacion():
    return render_template("automatizacion.html")

@app.route("/estadisticas")
def estadisticas():
    return render_template("estadisticas.html")

if __name__ == "__main__":
    app.run(debug=True)