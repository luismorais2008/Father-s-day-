import os
import time 


os.system("python3 build_video.py")
time.sleep(2)
os.system("python3 build_heart.py")
time.sleep(2)
os.system("python3 play_video.py")
time.sleep(2)  
os.system("python3 speak.py")

