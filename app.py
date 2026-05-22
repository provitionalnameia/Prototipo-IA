import os
from flask import Flask, render_template

# Localización absoluta y segura del directorio de plantillas para evitar el error TemplateNotFound en Render
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def home():
    return render_template("index.html")

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
    # Recuerda desactivar debug=True (cambiarlo a False) antes de pasar a producción definitiva
    app.run(debug=True)