from package.skills.core import speak
import random

def Ball():
    speak.Speak('Кристальний шар баче майбутьнє')
    speak.Speak('Задавайте питання')
    while True:
        a=['кінець', 'дякую за магію','стоп']
        b=speak.listen_command()
        h='Ти найкращий?'
        if b in a:
            break
        elif b == ' ':
            continue
        elif h==b:
            print('Так')
            speak.Speak('так')
        else:
            k=['Так','Ні','Можливо','Не знаю']
            x=random.choice(k)
            speak.Speak(x)
            print(x)
    speak.Speak('Сеанс закінчено')
    print('Сеанс закінчено')
