from flask import Flask, send_from_directory, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.get("/api/excel")
def get_excel(anno: int = None):

    df = pd.read_excel("dati.xlsx")

    if anno:
        df = df[df["Anno"] == anno]

    return df.to_dict(orient="records")

if __name__ == "__main__":
    app.run()
