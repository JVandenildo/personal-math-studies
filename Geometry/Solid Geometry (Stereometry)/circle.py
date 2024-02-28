from numpy import pi


class circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return round(2 * self.radius, 2)

    def area(self):
        return round(pi * (self.radius**2), 2)

    def circumference(self):
        return round(2 * pi * self.radius, 2)


NeoCircle = circle(float(input("Radius: ")))
print(
    f"Diameter: {NeoCircle.diameter()};\nArea: {NeoCircle.area()};\nCircumference: {NeoCircle.circumference()}."
)
