from flask import Flask, render_template, request
from ensembl_api import build_variant_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        rsid = request.form.get("rsid")
        result = build_variant_response(rsid)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


