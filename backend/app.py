from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Para facilitar pruebas desde otros orígenes si hace falta

# Datos de ejemplo (no usamos base de datos aquí)
GAMES = [
    {
        "id": 1,
        "title": "The Legend of Flask",
        "year": 2024,
        "genre": "Aventura",
    },
    {
        "id": 2,
        "title": "Cloud Quest",
        "year": 2023,
        "genre": "RPG",
    },
    {
        "id": 3,
        "title": "Docker Dash",
        "year": 2022,
        "genre": "Plataformas",
    },
]


@app.route("/")
def index():
    """
    Devuelve la página principal (HTML) que cargará el JS
    y pedirá los juegos a la API /api/games.
    """
    return render_template("index.html")


@app.route("/api/games")
def get_games():
    """
    Endpoint de prueba que simula un listado de videojuegos.
    Aquí no usamos base de datos, son datos en memoria.
    """
    return jsonify(GAMES)


@app.route("/api/health")
def health():
    """
    Endpoint muy simple para comprobar que el backend está vivo.
    Útil para pruebas rápidas en la nube.
    """
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # En producción el puerto y host pueden venir de variables de entorno
    app.run(host="0.0.0.0", port=8000, debug=True)
