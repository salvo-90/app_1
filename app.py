from flask import Flask, send_from_directory, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/api/excel")
def excel():
    df = pd.read_excel("dati.xlsx")
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run()
