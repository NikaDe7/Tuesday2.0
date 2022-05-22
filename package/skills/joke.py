import pyjokes
from googletrans import Translator
from package.skills.core import speak

translator = Translator()

def Joke():
    joke = pyjokes.get_joke()
    a = translator.translate(joke, dest='uk')
    speak.Speak(a.text)
    print(a.text)
