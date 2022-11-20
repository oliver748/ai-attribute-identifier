# creates all the necessary folders for it to work

import os

if not os.path.isdir("images"):
    os.mkdir("images")
    os.mkdir("images/asian")
    os.mkdir("images/white")
    os.mkdir("images/black")
    os.mkdir("images/latino")
    os.mkdir("images/middle-eastern")
    os.mkdir("images/indian")
if not os.path.isdir("temp"):
    os.mkdir("temp")
if not os.path.isdir("data"):
    os.mkdir("data")
