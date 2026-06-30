from flask import Flask, send_from_directory, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/api/excel")
def get_excel():

    anno = request.args.get("anno")

    df = pd.read_excel("dati.xlsx")

    if anno:
        df = df[df["Anno"] == int(anno)]

    return df.to_dict(orient="records")

if __name__ == "__main__":
    app.run()
