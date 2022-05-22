from package.skills.core import speak
import pyautogui
import datetime

def Screen():
    strTime = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    im1 = pyautogui.screenshot()
    x=str(strTime)+'.png'
    im1.save(r'C:\Users\vorob\OneDrive\Рабочий стол\tuesday\screen_shout\screen_'+x)
    speak.Speak('Готово')
    print('Готово')
