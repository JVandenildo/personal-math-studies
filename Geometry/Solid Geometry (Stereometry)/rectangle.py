class rectangle:
    def __init__(self, baseLength: float, heightLength: float) -> None:
        self.baseLength = baseLength
        self.heightLength = heightLength

    def diagonal(self) -> float:
        return round(((self.baseLength**2) + (self.heightLength**2)) ** (1 / 2), 2)

    def area(self) -> float:
        return round(self.baseLength * self.heightLength, 2)

    def perimeter(self) -> float:
        return round(2 * (self.baseLength + self.heightLength), 2)


NeoRectangle = rectangle(float(input("Base length: ")), float(input("Height length: ")))

print(
    f"Diagonal: {NeoRectangle.diagonal()};\nArea: {NeoRectangle.area()};\nPerimeter: {NeoRectangle.perimeter()}."
)
