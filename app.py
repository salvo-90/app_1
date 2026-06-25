from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# endpoint base
@app.route("/")
def home():
    return "API Excel attiva 🚀"

# endpoint che legge Excel
@app.route("/api/excel")
def get_excel():
    # legge file Excel
    df = pd.read_excel("dati.xlsx")

    # converte in JSON
    data = df.to_dict(orient="records")

    return jsonify(data)

# endpoint con filtro (utile)
@app.route("/api/excel/<colonna>/<valore>")
def filter_excel(colonna, valore):
    df = pd.read_excel("dati.xlsx")

    # filtro semplice
    df_filtrato = df[df[colonna].astype(str) == valore]

    return jsonify(df_filtrato.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
