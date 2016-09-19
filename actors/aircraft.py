import shared.constants as C

class Aircraft:
    """
    This class represents the aircraft controlled by the user.
    """
    def __init__(self, actor):
        self.actor = actor
        self.positionX = 60
        self.positionY = C.HEIGHT / 2
        self.acceleration = 0
        self.shape = 'circle'

    def draw(self):
        """
        Draw the aircraft in the screen.
        """
        self.actor.x = self.positionX
        self.actor.y = self.positionY
        self.actor.draw()

    def change_shape(self):
        self.shape = next(C.SHAPE)
        self.actor.image = 'aircraft-' + self.shape

    def go_ahead(self):
        if self.shape == 'square':
            self.positionX += 10

    def go_back(self):
        if self.shape == 'square':
            self.positionX -= 10
