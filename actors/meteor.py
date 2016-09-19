class Meteor:
    """
    This class represents the aircraft controlled by the user.
    """
    def __init__(self, actor, positionX, positionY,mass, speed, gravity=100):
        self.actor = actor
        self.positionX = positionX
        self.positionY = positionY
        self.mass = mass
        self.speed = speed
        self.gravity = gravity
        self.acceleration = 0
        self.area = self.actor.width * self.actor.height

    def draw(self):
        """
        Draw the aircraft in the screen.
        """
        self.actor.x = self.positionX
        self.actor.y = World.HEIGHT - self.positionY
        self.actor.draw()
