from numpy import pi


class pyramid:
    def __init__(self, height: float, baseSide: float, baseForm: str) -> None:
        self.height = height
        self.baseSide = baseSide
        self.baseForm = baseForm

    def area(self) -> float:
        if self.baseForm == "square":
            return 0
        if self.baseForm == "circle":
            return 0
        else:
            return 0

    def volume(self) -> float:
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
