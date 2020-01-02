import keyboard

def press(game):
    k1 = ['w','s','d','a']
    k2 = ['u','d','r','l']
    for key in range(4):
        if k2[key] not in game.snake.keys and keyboard.is_pressed(k1[key]):
            game.snake.keys.append(k2[key])
