from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# endpoint base
@app.route("/")
def home():
    return "API attiva 🚀"

# endpoint API semplice
@app.route("/api/hello")
def hello():
    return jsonify({"message": "ciao dal backend"})

# endpoint con parametro
@app.route("/api/saluto")
def saluto():
    nome = request.args.get("nome", "utente")
    return jsonify({"message": f"ciao {nome}"})

# endpoint con dati finti (simil BI)
@app.route("/api/dati")
def dati():
    return jsonify([
        {"anno": 2024, "valore": 100},
        {"anno": 2025, "valore": 150}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
