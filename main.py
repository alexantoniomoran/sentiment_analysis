import json

from textblob import TextBlob
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/sentiment_analysis", methods=["POST"])
def sentiment_analysis_of_text():
    json_obj = json.loads(request.data)
    text = json_obj["text"]
    blob = TextBlob(text)

    polarity = blob.sentiment.polarity
    if polarity > 0:
        return jsonify("Alex")

    if polarity < 0:
        return jsonify("Nick")

    return jsonify("Emily")


if __name__ == "__main__":
    app.run(port=8000)
