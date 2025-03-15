import torch
from transformers import pipeline
from flask import Flask, request, jsonify

# Load a small language model (TinyBERT for sentiment analysis & summarization)
summarizer = pipeline("summarization", model="facebook/bart-small")
sentiment_analyzer = pipeline("sentiment-analysis")

# Initialize Flask app
app = Flask(__name__)

@app.route("/summarize", methods=["POST"])
def summarize_text():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
    return jsonify({"summary": summary[0]['summary_text']})

@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    sentiment = sentiment_analyzer(text)
    return jsonify({"sentiment": sentiment[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
