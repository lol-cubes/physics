from physics.vectors import Vector


class Body:
    """
    Something that consists of matter

    Velocity is a vector whose magnitude is in m/s
    """

    def __init__(self, canvas, identifier, x, y, velocity=Vector(x=0, y=0), mass=1):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.id = identifier
        self.velocity = velocity
        self.mass = mass

    @property
    def coords(self):
        return self.x, self.y

    def move(self, t):
        """
        moves ball as far as it would go with current velocity in `t` seconds
        """
        horizontal_movement = int(self.velocity.horizontal_component * t)
        vertical_movement = int( - (self.velocity.vertical_component * t))

        self.canvas.move(self.id, horizontal_movement, vertical_movement)
        self.x += horizontal_movement
        self.y += vertical_movement

    def push(self, f, t):
        """
        Applies work to self with force `f` for duration `t`
        """
        a = f * (1 / self.mass)  # acceleration
        dv = a * t  # change in velocity
        self.velocity += dv
        self.move(t)