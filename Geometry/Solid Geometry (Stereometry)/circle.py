from numpy import pi


class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(pi * (self.radius**2), 2)


NeoCircle = circle(float(input("Radius: ")))
print(
    f"Area of a circle with {NeoCircle.radius} radius is {NeoCircle.area()} squared units."
)
