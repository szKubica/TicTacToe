from pygame_init import Game
import time


game1 = Game(3)
game1.draw()

while True:
    game1.set_computer()
    game1.set_player()


