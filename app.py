from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

def apply_query(df, args):
    # SELECT (colonne)
    if "$select" in args:
        cols = args.get("$select").split(",")
        df = df[cols]

    # FILTER (solo eq base)
    if "$filter" in args:
        filtro = args.get("$filter")
        campo, _, valore = filtro.partition(" eq ")
        df = df[df[campo].astype(str) == valore]

    # ORDER BY
    if "$orderby" in args:
        order = args.get("$orderby")
        parts = order.split()
        col = parts[0]
        asc = True if len(parts) == 1 or parts[1] == "asc" else False
        df = df.sort_values(by=col, ascending=asc)

    # TOP
    if "$top" in args:
        top = int(args.get("$top"))
        df = df.head(top)

    return df

@app.route("/api/excel")
def excel():
    df = pd.read_excel("dati.xlsx")

    # applica query stile OData
    df = apply_query(df, request.args)

    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
