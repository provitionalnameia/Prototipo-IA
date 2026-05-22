from flask import Flask, render_template
import os

template_dir = os.path.abspath('templates')

app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/atencion")
def atencion():
    return "<h1>Atención al cliente</h1>"

@app.route("/automatizacion")
def automatizacion():
    return "<h1>Procesos automáticos</h1>"

@app.route("/estadisticas")
def estadisticas():
    return "<h1>Estadísticas IA</h1>"

if __name__ == "__main__":
    app.run(debug=True)