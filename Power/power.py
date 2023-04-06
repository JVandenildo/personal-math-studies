a = int(input("Base number: "))
b = int(input("Power number: "))

def power(a, b):
    count = 1
    p = a

    while count < b:
        p = p * a
        count+=1
    
    return print(p)

power(a, b)
