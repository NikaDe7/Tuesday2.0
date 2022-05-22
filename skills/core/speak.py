import speech_recognition
import pyttsx3

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
sr.energy_threshold = 4000
sr.dynamic_energy_adjustment_ratio = 5
engine = pyttsx3.init()
engine.setProperty('voice', 'uk-UA')

class VoiceAssistant:
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1)
    engine.setProperty('voice', 'uk-UA')
    for voice in voices:
        if voice.name == 'Anatol':
            engine.setProperty('voice', voice.id)

def Speak(listen_command):
    engine.say(listen_command)
    engine.runAndWait()
    
def listen_command():
    global query
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='uk-UA').lower()
            return query
    except speech_recognition.UnknownValueError:
        Speak('Нічого не зрозумів')
        print('Нічого не зрозумів')
    return query
