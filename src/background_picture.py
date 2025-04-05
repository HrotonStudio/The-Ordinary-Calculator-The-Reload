from src.lib_usual import os, time, random
from src.settings import Background

if Background == "Default":
    picture = "./background/default.png"
elif Background == "Time":
    if time.localtime().tm_hour >= 6 and time.localtime().tm_hour <= 18:
        base_dir = "background\\time\\day"
        file_day = [os.path.join(base_dir, f) for f in os.listdir(base_dir)]
        picture = random.choice(file_day)
    else:
        base_dir = "background\\time\\night"
        file_night = [os.path.join(base_dir, f) for f in os.listdir(base_dir)]
        picture = random.choice(file_night)
else:
    picture = "./background/default.png"