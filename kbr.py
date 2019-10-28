import keyboard
def press(d):
    keys = ['w','s','d','a','i','l','k','j','t','g','f','h']
    for key in keys:
        if key not in d:
            if keyboard.is_pressed(key):
                d.append(key)
    return d
    