import keyboard

def key_check():
    if keyboard.is_pressed("A"):
        return "A"
    if keyboard.is_pressed("W"):
        return "W"
    if keyboard.is_pressed("B"):
        return "B"
    if keyboard.is_pressed("L"):
        return "L"
    if keyboard.is_pressed("M"):
        return "M"
    if keyboard.is_pressed("I"):
        return "I"
    if keyboard.is_pressed("S"):
        return "S"
    if keyboard.is_pressed("D"):
        return "D"
    