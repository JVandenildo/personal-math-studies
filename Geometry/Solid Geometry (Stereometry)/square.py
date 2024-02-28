class square:
    def __init__(self, baseLength: float, heightLength: float) -> None:
        self.baseLength = baseLength
        self.heightLength = heightLength

    def area(self) -> float:
        return round(self.baseLength * self.heightLength, 2)

    def diagonal(self) -> float:
        return round(((self.baseLength**2) + (self.heightLength**2)) ** (1 / 2), 2)


NeoSquare = square(float(input("Base length: ")), float(input("Height length: ")))

print(f"Area: {NeoSquare.area()};\nDiagonal: {NeoSquare.diagonal()}.")
