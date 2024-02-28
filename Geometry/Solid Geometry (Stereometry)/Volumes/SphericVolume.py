from numpy import pi


class sphere:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def volume(self):
        return round(pi * (self.radius**3) * (4 / 3), 2)


NeoSphere = sphere(float(input("Radius: ")))

print(NeoSphere.volume())
