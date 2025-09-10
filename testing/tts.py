import pyttsx3

def speak(text):
    e=pyttsx3.init()
    e.setProperty('volume', 1.2)
    e.save_to_file(text,'vc.mp3')
    e.runAndWait()

speak("Hello")