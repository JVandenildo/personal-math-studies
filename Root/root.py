def root(base, b):
    r = 1

    while r != base:
        p = r
        count = 1

        while count < b:
            p = p * r
            count+=1
            if p == base:
                return r

        if r == base:
            return r
        else:
            r = r + 1
    
    return r

base = int(input("Base number: "))
b = int(input("Root number: "))

# some combinations doesn't return the correct result; be aware
print(f'Root of {base} by {b} is {root(base, b)}.')