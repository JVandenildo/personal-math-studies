class cube:
    def __init__(self, faceArea: float):
        self.faceArea = faceArea

    def selfVolume(self):
        return round(pow(self.faceArea, 3), 2)


NeoCube = cube(float(input("Area's face: ")))
print(NeoCube.selfVolume())
