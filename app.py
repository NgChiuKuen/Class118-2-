from flask import Flask, render_template, request, jsonify
from model_prediction import *

app = Flask(__name__)

text=""
predicted_emotion=""
predicted_emotion_img_url=""

@app.route("/")
def home():
    entries = show_entry()
    return render_template("index.html", entries=entries)
    

@app.route("/predict-emotion", methods=["POST"])
def predict_emotion():
    input_text = request.json.get("text")
    if not input_text:
        return jsonify({
            "status": "error",
            "message": "Please enter some text to predict emotion!"
        }), 400
    else:
        predicted_emotion, predicted_emotion_img_url = predict(input_text)                         
        return jsonify({
            "data": {
                "predicted_emotion": predicted_emotion,
                "predicted_emotion_img_url": predicted_emotion_img_url
            },
            "status": "success"
        }), 200
        
#Write the code for API here
@app.route('/save-data', methods=['POST'])
def save_data():
    date = request.json.get("date")
    text = request.json.get("text")
    emotion = request.json.get("emotion")

    text = text.replace("\n"," ")
    data = f'"{date}","{text}","{emotion}"\n'

    with open('static/assets/data_files/data_entry.csv') as var1:
       var1.write(data)     
    return jsonify("Success")



if __name__ == "__main__":
    app.run(debug=True)

