from numpy import pi


def areaCircle(radius):
    return round(pi * (radius**2), 2)


r = float(input("Radius: "))
print(f"Area of a circle with {r} radius is {areaCircle(r)} squared units.")
