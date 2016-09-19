import sys; sys.path.append('.')
from FGAme import *
from actors.aircraft import Aircraft
from stages.one import World
import shared.constants as C

TITLE = "SHAPE"
SPEED = 3

aircraft = Aircraft(
    Actor('aircraft-circle')
)

world.add.margin(10)

def draw():
    screen.blit('background', pos=(0, 0))
    aircraft.draw()

def update(dt):
    if keyboard.space:
        aircraft.change_shape()
    if (aircraft.shape == 'triangle'):
        if keyboard.right:
            aircraft.go_ahead()
        if keyboard.left:
            aircraft.go_back()
    elif (aircraft.shape == 'circle'):
        aircraft.circleMove(dt)



