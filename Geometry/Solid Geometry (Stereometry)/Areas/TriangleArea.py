def triangleArea(height, base):
    return round(height * base / 2, 2)


height = float(input("Height: "))
base = float(input("Base: "))

print(triangleArea(height, base))
