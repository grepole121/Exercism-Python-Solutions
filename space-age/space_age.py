earth = 31557600
mercury = earth * 0.2408467
venus = earth * 0.61519726
mars = earth * 1.8808158
jupiter = earth * 11.862615
saturn = earth * 29.447498
uranus = earth * 84.016846
neptune = earth * 164.79132

class SpaceAge:
    def __init__(self, seconds):
        self.s = seconds

    def on_earth(self):
        return round(self.s/earth,2)

    def on_mercury(self):
        return round(self.s/mercury,2)

    def on_venus(self):
        return round(self.s/venus,2)

    def on_mars(self):
        return round(self.s/mars,2)

    def on_jupiter(self):
        return round(self.s/jupiter,2)

    def on_saturn(self):
        return round(self.s/saturn,2)

    def on_uranus(self):
        return round(self.s/uranus,2)

    def on_neptune(self):
        return round(self.s/neptune,2)