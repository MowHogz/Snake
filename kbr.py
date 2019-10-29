import keyboard
def press(d):
    keys = ['w','s','d','a','e','i','l','k','j','o','t','g','f','h','y']
    for key in keys:
        if key not in d:
            if keyboard.is_pressed(key):
                d.append(key)
    return d
    