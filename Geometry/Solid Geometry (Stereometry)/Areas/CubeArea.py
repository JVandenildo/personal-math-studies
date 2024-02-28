# area for the surface of a cube
def CubeArea(number):
    return 6 * (number**2)


vertices = float(input("Size of a vertices: "))

print(f"Area of a cube with vertices {vertices} is {CubeArea(vertices)} squared units.")
