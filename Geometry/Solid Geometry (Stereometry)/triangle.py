class triangle:
    def __init__(self, height: float, base: float) -> None:
        self.height = height
        self.base = base

    def area(self) -> float:
        return round(self.height * self.base / 2, 2)


NeoTriangle = triangle(float(input("Height: ")), float(input("Base: ")))


print(f"Area: {NeoTriangle.area()}.")
