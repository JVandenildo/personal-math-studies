class cube:
    def __init__(self, verticeHeight: float) -> None:
        self.verticeHeight = verticeHeight

    def volume(self) -> float:
        facesArea = self.verticeHeight**2

        return round(pow(facesArea, 3), 2)

    def area(self) -> float:
        return 6 * (self.verticeHeight**2)


NeoCube = cube(float(input("Vertice height: ")))
print(f"Volume: {NeoCube.volume()};\nArea of a face: {NeoCube.area()}.")
