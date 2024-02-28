from numpy import pi


def SphereArea(radius):
    return round(4 * pi * (pow(radius, 2)), 2)


radius = float(input("Radius: "))
print(f"Area of the sphere's surface is {SphereArea(radius)}.")
