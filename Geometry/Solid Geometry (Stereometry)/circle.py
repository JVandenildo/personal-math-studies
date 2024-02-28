from numpy import pi


class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(pi * (self.radius**2), 2)

    def diameter(self):
        return round(pi * self.radius, 2)


NeoCircle = circle(float(input("Radius: ")))
print(f"Area: {NeoCircle.area()};\nDiameter: {NeoCircle.diameter()}.")
