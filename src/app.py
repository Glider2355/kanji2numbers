import os
import sys
import urllib.parse

sys.path.append('..')

from flask import Flask, render_template, make_response, jsonify
from number2kanji import number2kanji as n2k
from kanji2number import kanji2number as k2n

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# templates/index.htmlを表示
@app.route("/", methods=["GET"])
def top_page():
    return render_template("index.html")


@app.route("/v1/number2kanji/<number>", methods=["GET"])
def number2kanji(number):
    try:
        return str(n2k(number))
    except:
        return make_response("", 204)


@app.route("/v1/kanji2number/<kanji>", methods=["GET"])
def kanji2number(kanji):
    try:
        return str(k2n(kanji))
    except:
        return make_response("", 204)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), threaded=True)
