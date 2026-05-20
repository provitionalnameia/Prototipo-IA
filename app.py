from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/atencion")
def atencion():
    return """
    <h1 style='color:white;
    font-family:Arial;
    text-align:center;
    margin-top:100px;
    background:black;'>
    Página de atención al cliente próximamente
    </h1>
    """

@app.route("/automatizacion")
def automatizacion():
    return """
    <h1 style='color:white;
    font-family:Arial;
    text-align:center;
    margin-top:100px;
    background:black;'>
    Página de procesos próximamente
    </h1>
    """

@app.route("/estadisticas")
def estadisticas():
    return """
    <h1 style='color:white;
    font-family:Arial;
    text-align:center;
    margin-top:100px;
    background:black;'>
    Página de estadísticas próximamente
    </h1>
    """

if __name__ == "__main__":
    app.run(debug=True)