"""
This module initializes a Flask application for emotion detection.

It defines two routes:
1. /emotionDetector: Analyzes the emotion of the given text.
2. /: Renders the index page.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detection")

@app.route("/emotionDetector", methods=["GET"])
def sent_detector():
    """Endpoint to analyze the emotion of the given text."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze."

    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid input! Try again."

    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is {dominant_emotion}: {response}"

@app.route("/", methods=["GET"])
def render_index_page():
    """Endpoint to render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
