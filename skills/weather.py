from package.skills.core import speak
from pyowm.utils.config import get_default_config 
import pyowm

config_dict = get_default_config()
config_dict['language'] = 'uk'
owm = pyowm.OWM('21c66c39fdafae690ceae27bdfcc47f0', config_dict)
mgr = owm.weather_manager()

def Weather():
    observation= mgr.weather_at_place('Lviv, UA')
    w = observation.weather
    print('Статус на сьогодні')
    speak.Speak('Подивіться на результат')
    data = {
        '[Загалом]':w.detailed_status,
        '[Швидкість повітря{м/с)]':w.wind()['speed'],
        '[Температура(С°)]':w.temperature('celsius')['temp'],
        '[Вологість(%)]':w.humidity,
        '[Хмарність(%)]':w.clouds}
    for u,h in data.items():
        print(f'{u} : {h}')
    print ('Це все')
    speak.Speak('Це все')
    print('Вам цікаво, що буде завтра?')
    speak.Speak('Вам цікаво, що буде завтра?')
    j=['звичайно','так','давай']
    n=speak.listen_command()
    if n in j:
        Tomorrow()
    else:
        speak.Speak('Як скажете')
        print('Як скажете') 

def Tomorrow():
    speak.Speak('Я бачу майбутьнє')
    print('Cтатус на завтра')
    one_call = mgr.one_call(lat=47.8932, lon=31.0913)
    speak.Speak('Подивіться на результат')
    dat = {
        '[Статус]':one_call.forecast_daily[0].detailed_status,
        '[Швидкість повітря(м/с)]':one_call.forecast_daily[0].wind()["speed"],
        '[Температура(С°)]':one_call.forecast_daily[0].temperature('celsius').get('day', None),
        '[Вологість(%)]':one_call.forecast_daily[0].humidity,
        '[Хмарність(%)]':one_call.forecast_daily[0].clouds
    }
    for m,n in dat.items():
        print(f'{m} : {n}')
    speak.Speak('Тепер ти знаєщ, що буде завтра')
    print('Це все')
