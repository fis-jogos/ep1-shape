import shared.constants as C

class Aircraft:
    """
    This class represents the aircraft controlled by the user.
    """
    def __init__(self, actor):
        self.actor = actor
        self.positionX = C.MINIMAL_X
        self.positionY = C.HEIGHT / 2
        self.acceleration = 0
        self.shape = 'circle'
        self.vx = 100
        self.directionY = 1
        self.directionX = 1

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
        if self.shape == 'triangle':
            if self.positionX <= C.MAXIMAL_X:
                self.positionX += 10

    def go_back(self):
        if self.shape == 'triangle':
            if self.positionX >= C.MINIMAL_X:
                self.positionX -= 10

    def circleMove(self, dt):
        if self.directionY == 1:
            if self.positionY <= 550:
                self.positionY += C.GRAVITY * dt
            else:
                self.directionY = -1
        else:
            if self.positionY >= 45:
                self.positionY -= C.GRAVITY * dt
            else:
                self.directionY = 1

        if self.directionX == 1:
            if self.positionX <= C.MAXIMAL_X:
                self.positionX += self.vx * dt
            else:
                self.directionX = -1
        else:
            if self.positionX >= C.MINIMAL_X:
                self.positionX -= self.vx * dt
            else:
                self.directionX = 1
