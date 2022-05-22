from package.skills.core import speak

def Create_tack():
    speak.Speak('Що дописати до заміток?')
    print('Що дописати до заміток?')
    query = speak.listen_command()
    with open(r'C:\Users\vorob\OneDrive\Рабочий стол\tuesday\list.txt', 'a') as file:
        file.write(f'* {query}\n')
    speak.Speak('Замітка')
    speak.Speak(query)
    speak.Speak('додана до списку')
    print('Замітка ', query, ' додана до списку!')

