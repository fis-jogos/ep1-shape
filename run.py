import sys; sys.path.append('.')
from FGAme import *
from actors.aircraft import Aircraft
from stages.one import World
import shared.constants as C

TITLE = "SHAPE"
GRAVITY = 500
SPEED = 3

aircraft = Aircraft(
    Actor('aircraft-circle')
)

def draw():
    screen.blit('background', pos=(0, 0))
    aircraft.draw()

def update(dt):
    if keyboard.right:
        aircraft.go_ahead()
    if keyboard.left:
        aircraft.go_back()
    if keyboard.space:
        aircraft.change_shape()


