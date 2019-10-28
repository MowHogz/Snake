import keyboard
def press(d):
    keys = ['w','s','d','a']
    for key in keys:
        if keyboard.is_pressed(key):
            return key
    return d
    