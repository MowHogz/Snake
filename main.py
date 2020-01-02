import time 
from game import game
import threading
from kbr import press
def prs():
    while True:
        press(game)

game = game(20,20)
keys = threading.Thread(target=(prs))
keys.start()

while True:
    game.frame()
    time.sleep(0.1)