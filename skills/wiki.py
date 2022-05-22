import wikipedia
from package.skills.core import speak

def Wiki():
    speak.Speak('Що шукати у Вікіпедії?')
    print('Що шукати у Вікіпедії?')
    query = speak.listen_command()
    wikipedia.set_lang("uk") 
    wikip = wikipedia.page(query).content
    speak.Speak('Згідно з вікіпедією ')
    speak.Speak(wikip)
    print(wikip)
