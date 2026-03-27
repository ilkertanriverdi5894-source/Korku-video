from flask import Flask, jsonify
from gtts import gTTS

app = Flask(__name__)

@app.route("/")
def home():
    return "Server çalışıyor"

@app.route("/video")
def create_video():

    text = "Saat 03:00'tü... kapı yavaşça açıldı..."

    tts = gTTS(text, lang='tr')
    tts.save("ses.mp3")

    return jsonify({
        "durum": "ses oluşturuldu",
        "hikaye": text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
