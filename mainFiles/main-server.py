from flask import Flask, request
import os
from playsound import playsound  # pip install playsound==1.2.2
import threading

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def play_audio(path):
    playsound(path)

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, f.filename)
    f.save(path)

    threading.Thread(target=play_audio, args=(path,), daemon=True).start()
    return "Playing " + f.filename

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
