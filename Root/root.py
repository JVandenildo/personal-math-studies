a = int(input("Base number: "))
b = int(input("Root number: "))

def bloody(a, b):
    array = []
    r = 2
    i = a

    while i > 1:
        if i % r == 0:
            array.append(r)
            i = i / r

        else:
            array = []
            i = a
            r = r + 1

            if i == 1 and len(array) != b:
                i = a
                r = r + 1

    return r

# only works with perfect roots
print(f'Root of {a} by {b} is {bloody(a, b)}.')
