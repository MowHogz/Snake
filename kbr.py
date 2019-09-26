import keyboard 
def press(d):
    if keyboard.is_pressed('w'):
        return 'u'
    elif keyboard.is_pressed('s'):
        return 'd'
    elif keyboard.is_pressed('d'):
        return 'r'
    elif keyboard.is_pressed('a'):
        return 'l'
    return d
def presser(d):
    if keyboard.is_pressed('w'):
        if 'u' not in d:
            d.append('u')
    if keyboard.is_pressed('s'):
        if 'd' not in d:
            d.append('d')
    if keyboard.is_pressed('d'):
        if 'r' not in d:
            d.append('r')
    if keyboard.is_pressed('a'):
        if 'l' not in d:
            d.append('l')
    if keyboard.is_pressed('q'):
        if 'q' not in d:
            d.append('q')
    return d
def pressrl(d):
    if keyboard.is_pressed('d') or keyboard.is_pressed('w'):
        return 'u'
    elif keyboard.is_pressed('s') or keyboard.is_pressed('a'):
        return 'd'
    elif keyboard.is_pressed('q'):
        return 'q'
    else:
        return d