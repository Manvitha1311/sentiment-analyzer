from flask import Flask, render_template, request
from utils.model import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    confidence = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        sentiment, confidence = analyze_sentiment(text)

    return render_template(
        "index.html",
        sentiment=sentiment,
        confidence=confidence,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=True)
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)