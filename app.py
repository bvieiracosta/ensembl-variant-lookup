from flask import Flask, render_template, request
from ensembl_api import build_variant_response
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        rsid = request.form.get("rsid")

        try:
            result = build_variant_response(rsid)

        except ValueError as e:
            error = str(e)

        except requests.exceptions.RequestException:
            error = "Erro de conexão com a API do Ensembl"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
