#import core.speak
from package.skills.core import speak
import randfacts
from googletrans import Translator

translator = Translator()

def Facts():
    f = randfacts.get_fact(False)
    a= translator.translate(f, dest='uk')
    print(a.text)
    speak.Speak(a.text)


      
#Facts()
