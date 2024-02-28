def areaSquare(side):
    return round(side * side, 2)


side = float(input("Side length: "))

print(f"Area of a square by side {side} is {areaSquare(side)} squared units.")
