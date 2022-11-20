# this code is to actually use the model

import cv2
from utilities.grab_screen import grab_screen
from fastai.vision.all import *

def label_func(x): 
    return x.parent.name

print("Waiting for Learner")
learn_inf = load_learner("C:/Users/oliver/Desktop/race-identifier/export.pkl")
print("Loaded Learner")

# Wait for me to push S to start.
input('Press ENTER to start\n')



while True:
    screen_grab = grab_screen(region=(775, 220, 1750, 1225))
    image = cv2.resize(screen_grab, (150, 150)) # resizing gives much better results
    cv2.imwrite("a.png", image)
    prediction = learn_inf.predict(image)
    action = prediction[0]
    print(f"Race: {action.capitalize()}")
    input('')

