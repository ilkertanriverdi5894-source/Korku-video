from flask import Flask, jsonify
import requests
from moviepy.editor import *
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Server çalışıyor"

@app.route("/video")
def create_video():

    # 🎬 HİKAYE (şimdilik sabit, sonra AI ekleriz)
    text = "Saat 03:00'tü... kapı yavaşça açıldı... ama içeride kimse yoktu."

    # 🔊 SES OLUŞTUR
    tts = gTTS(text, lang='tr')
    tts.save("ses.mp3")

    # 🖼️ GÖRSEL ÇEK
    img_url = "https://images.pexels.com/photos/213162/pexels-photo-213162.jpeg"
    img_data = requests.get(img_url).content

    with open("bg.jpg", "wb") as f:
        f.write(img_data)

    # 🎞️ VİDEO OLUŞTUR
    audio = AudioFileClip("ses.mp3")
    image = ImageClip("bg.jpg").set_duration(audio.duration)

    video = image.set_audio(audio)
    video.write_videofile("video.mp4", fps=24)

    # 🧹 TEMİZLİK (opsiyonel)
    try:
        os.remove("ses.mp3")
        os.remove("bg.jpg")
    except:
        pass

    return jsonify({
        "durum": "video hazır",
        "hikaye": text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
