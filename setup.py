# creates all the necessary folders for it to work

import os

if not os.path.isdir("images"):
    os.mkdir("images")
if not os.path.isdir("temp"):
    os.mkdir("temp")
if not os.path.isdir("data"):
    os.mkdir("data")
