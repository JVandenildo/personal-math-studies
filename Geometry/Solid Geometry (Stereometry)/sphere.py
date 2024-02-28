from numpy import pi


class sphere:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def volume(self):
        return round(pi * (self.radius**3) * (4 / 3), 2)

    def area(self):
        return round(4 * pi * (pow(self.radius, 2)), 2)


NeoSphere = sphere(float(input("Radius: ")))

print(f"Volume: {NeoSphere.volume()};\nSurface area: {NeoSphere.area()}.")
