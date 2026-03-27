from flask import Flask, jsonify, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/")
def home():
    return "Server çalışıyor"

@app.route("/video")
def create_story_audio():
    text = "Saat 03:00'tü... telefona gelen mesajda sadece tek bir kelime yazıyordu: kapıyı açma."

    file_id = str(uuid.uuid4())
    mp3_path = os.path.join(OUTPUT_DIR, f"{file_id}.mp3")

    tts = gTTS(text, lang="tr")
    tts.save(mp3_path)

    return jsonify({
        "durum": "ses oluşturuldu",
        "hikaye": text,
        "ses_linki": f"/audio/{file_id}"
    })

@app.route("/audio/<file_id>")
def get_audio(file_id):
    mp3_path = os.path.join(OUTPUT_DIR, f"{file_id}.mp3")
    if not os.path.exists(mp3_path):
        return jsonify({"hata": "Dosya bulunamadı"}), 404
    return send_file(mp3_path, mimetype="audio/mpeg")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
