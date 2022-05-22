from package.skills.core import speak
import webbrowser

def YouTB():
    print('Що шукати?')
    speak.Speak('Що шукати?')
    search_term = speak.listen_command()
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
    speak.Speak('Зайдіть до вашого браузера')
    print('Зайдіть до вашого браузера')

def Browser():
    print('Що шукати?')
    speak.Speak('Що шукати?')
    r=speak.listen_command()
    url = "https://www.google.com/search?q=" + r
    webbrowser.get().open(url)
    speak.Speak('Зайдіть до вашого браузера')
    print('Зайдіть до вашого браузера')
