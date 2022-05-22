from package.skills.core import speak
import datetime

def Time():
    strTime = datetime.datetime.now().strftime('%H:%M')
    speak.Speak('Зараз')
    speak.Speak(strTime)
    print(strTime)

