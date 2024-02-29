class cube:
    def __init__(
        self, heightVertice: float, baseVertice: float, deepVertice: float
    ) -> None:
        self.heightVertice = heightVertice
        self.baseVertice = baseVertice
        self.deepVertice = deepVertice

    def surfaceArea(self) -> float:
        return (
            (2 * (self.baseVertice * self.heightVertice))
            + (2 * (self.baseVertice * self.deepVertice))
            + (2 * (self.heightVertice * self.deepVertice))
        )

    def volume(self) -> float:
        return round(self.baseVertice * self.heightVertice * self.deepVertice, 2)


NeoCube = cube(
    float(input("Height length: ")),
    float(input("Base length: "), float(input("Deep length: "))),
)
print(f"Surface area: {NeoCube.area()};\n;Volume: {NeoCube.volume()}.")
