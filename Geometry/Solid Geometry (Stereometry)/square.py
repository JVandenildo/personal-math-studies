class square:
    def __init__(self, vertice: float):
        self.vertice = vertice

    def area(self):
        return round(self.vertice**2, 2)


NeoSquare = square(float(input("Vertice length: ")))

print(
    f"Area of a square by side {NeoSquare.vertice} is {NeoSquare.area()} squared units."
)
