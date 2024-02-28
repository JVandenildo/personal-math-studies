class cube:
    def __init__(self, verticeHeight: float):
        self.verticeHeight = verticeHeight

    def volume(self):
        facesArea = self.verticeHeight**2

        return round(pow(facesArea, 3), 2)

    def area(self):
        return 6 * (self.verticeHeight**2)


NeoCube = cube(float(input("Vertice height: ")))
print(f"Volume: {NeoCube.volume()};\nArea of a face: {NeoCube.area()}.")
