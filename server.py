"""importing flask framework & emotion_detector app"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
'''defining app route & user interface output'''
@app.route("/emotionDetector")
def emo_dectector():
    """emotion detector app test"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion= response['Dominant emotion']
    all_emotions= response
    all_emotions.pop('Dominant emotion')
    if dominant_emotion is None:
        return "Invalid input ! Try again."
    else:
        return "For the given statement, the system response is {}.The dominant emotion is {}".format(str(all_emotions).replace("{","").replace("}",""),dominant_emotion)
@app.errorhandler(500)
def internal_error():
    """internal error handling"""
    return "Invalid text! Please try again!"
@app.route("/")
def render_index_page():
    """referencing index page and port"""
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
