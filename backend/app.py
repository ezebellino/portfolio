from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/projects")
def get_projects():
    return jsonify([
        {
            "id": 1,
            "title": "Portfolio Website",
            "description": "Sitio personal hecho con React y Flask.",
            "url": "https://github.com/ezebellino/portfolio"
        },
        {
            "id": 2,
            "title": "API de Ejemplo",
            "description": "Una REST API simple hecha con Flask.",
            "url": "https://github.com/ezebellino/api-clima"
        }
    ])

if __name__ == "__main__":
    app.run(debug=True)
