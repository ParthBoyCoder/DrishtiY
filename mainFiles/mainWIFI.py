import base64
import requests
import RPi.GPIO as GPIO
import time
import wget
import pyttsx3
import re

PRM="The image u r given is what a blind person is pointing at. describe the scene to the blind person. be descriptive."

ESP32CAM=""

API_KEY = ''

PC_IP=""

BUTTON_PIN = 17

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"



e = pyttsx3.init()

voices = e.getProperty("voices")

if voices:
    e.setProperty("voice", voices[1].id) #change (voices[x]) x as you need
else:
    print("NO VC FOUND!")

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def gem(prm, img):
    image_b64 = image_to_base64(img)

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prm
                    },
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_b64
                        }
                    }
                ]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(URL, headers=headers, json=payload)
    data=response.json()
    return (data['candidates'][0]['content']['parts'][0]['text'])

def playA(filename):
    url = f"http://{PC_IP}:5000/upload"
    with open(filename, 'rb') as f:
        files = {'file': (filename, f)}
        r = requests.post(url, files=files)

    print("Triggered:", r.status_code)
    if r.status_code == 200:
        print(f"Uploaded and playing {filename} on PC website!")
    else:
        print("Error:", r.text)

def speak(text):
    e.setProperty('volume',1.0)
    e.save_to_file(text,'vc.wav')
    e.runAndWait()

def remove_symbols(text: str) -> str:
    # keep only letters, numbers, and spaces
    return re.sub(r'[^A-Za-z0-9 ]+', '', text)

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # button pressed
            wget.download(ESP32CAM+"/capture", "capture.jpg")
            o=remove_symbols(gem(PRM,"capture.jpg"))
            speak(o)
            time.sleep(3)
            playA("vc.wav")
        time.sleep(0.3)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()