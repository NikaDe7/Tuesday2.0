import os
import random
from package.skills.core import speak

def Play_music():
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    speak.Speak('Слухаєм')
    speak.Speak(random_file.split("/")[-1])
    os.system(f'start {random_file}')
    print('Слухаєм', {random_file.split("/")[-1]})
