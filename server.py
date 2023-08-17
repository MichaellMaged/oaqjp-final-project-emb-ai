from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_dectector():
     text_to_analyze = request.args.get('textToAnalyze')
     response = emotion_detector(text_to_analyze)
     all_emotions=response['anger', 'disgust', 'fear','joy', 'sadness']
     dominant_emotion=response['Dominant Emotion']

     if emotion_name is None:
        return "Invalid input ! Try again."
     else:
        return "For the given statement, the system response is {}.The dominant emotion is {}".format(all_emotions,dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    