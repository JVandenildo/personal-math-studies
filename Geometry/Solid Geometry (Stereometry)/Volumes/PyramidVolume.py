from numpy import pi


class pyramid:
    def __init__(self, height: float, baseSide: float, baseForm: str):
        self.height = height
        self.baseSide = baseSide
        self.baseForm = baseForm

    def volume(self):
        if self.baseForm == "square":
            return round((self.height * (pow(self.baseSide, 2))) / 3, 2)

        elif self.baseForm == "circle":
            return round((self.height * (pi * (pow(self.baseSide, 2)))) / 3, 2)

        else:
            return 0


NeoPyramid = pyramid(
    float(input("Height: ")),
    float(input("Base side: ")),
    str(input("circle or square? ")),
)

print(NeoPyramid.volume())
