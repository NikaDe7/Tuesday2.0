from package.skills.core import speak
import random

def Story():
    Sentence_starter = ['Сто років вперед,', 'Діло буде в 41 році,', 'В один прекрасний період часу,']
    character = [' житиме король.',' житиме фермер.', ' житиме Антон.', ' житиме Маргарет.']
    time = [' В один прекрасний день', ' Опівночі', ' Після обіду']
    story_plot = [', роздумуючи про життя,',', йшовши на пікнік,']
    place = [' в горах,', ' в саду,', ' на озері,']
    second_character = [' бачить чоловіка.', ' побачить незнайомку.']
    work = [' Коли стало нудно,', ' Коли стало цікаво,']
    run = [' захотілось спитатися, "як звати"?, але людина вже втекла.']
    end = [' Не вийде зустрітись їм знову навіть, коли',' Зустрінуться вони, коли']
    tim = [' пройде 100 років',' настане час']

    m=random.choice(Sentence_starter)+random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(place)+random.choice(second_character)+random.choice(work)+random.choice(run)+random.choice(end)+random.choice(tim)
    print(m)
    speak.Speak(m)
    speak.Speak('Кінець')
    print('Кінець')
