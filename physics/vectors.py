import math


class Vector:
    """
    A quantity with both direction and magnitude

    2 possible ways of instantiating:
     - cartesian coordinates (`p1`, `p2`)
     - polar coordinates (`direction`, `magnitude`)
    """

    @classmethod
    def get_magnitude(cls, x, y):
        """
        finds length of vector using distance formula
        """
        return math.sqrt((x ** 2) + (y ** 2))

    @classmethod
    def get_direction(cls, x, y):
        """
        finds angle of vector from coords
        """
        return math.degrees(math.atan(y / x))

    @classmethod
    def get_horizontal_component(cls, r, theta):
        """
        finds horizontal component (x coord) 
        of vector from polar coords
        """
        return r * math.cos(math.radians(theta))

    @classmethod
    def get_vertical_component(cls, r, theta):
        """
        finds vertical component (y coord)
        of vector from polar coords
        """
        return r * math.sin(math.radians(theta))


    def __init__(self, **kwargs):

        if (keys := set(kwargs.keys())) == {"theta", "r"}:
            # polar coords
            self.type = "polar"
            self.theta = kwargs["theta"]
            self.r = kwargs["r"]
        
        elif keys == {"x", "y"}:
            # cartesian coords
            self.type = "cartesian"
            self.x = kwargs["x"]
            self.y = kwargs["y"]

        else:
            raise ValueError
        
    @property
    def magnitude(self):
        if self.type == "polar":
            return self.r
        elif self.type == "cartesian":
            return Vector.get_magnitude(self.x, self.y)
    
    @property
    def direction(self):
        if self.type == "polar":
            return self.theta
        elif self.type == "cartesian":
            return Vector.get_direction(self.x, self.y)

    @property
    def horizontal_component(self):
        if self.type == "polar":
            return Vector.get_horizontal_component(self.r, self.theta)
        elif self.type == "cartesian":
            return self.x

    @property
    def vertical_component(self):
        if self.type == "polar":
            return Vector.get_vertical_component(self.r, self.theta)
        elif self.type == "cartesian":
            return self.y

    def __add__(self, other):
        return Vector(
            x=(self.horizontal_component + other.horizontal_component),
            y=(self.vertical_component + other.vertical_component))

    def __str__(self):
        return f"theta = {self.direction}\nr = {self.magnitude}\nx = {self.horizontal_component}\ny = {self.vertical_component}"