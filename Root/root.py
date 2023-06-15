def root(base, b):
    r = 1

    while r <= base / 2:
        p = r
        count = 1

        while count <= b:
            p = p * r
            count += 1
            if p == base and count == b:
                answer = f"{r}"

                return answer
        r = r + 1

    if p == base and count == b:
        answer = f"{r}"
    else:
        answer = "a non integer"

    return answer


base = int(input("Base number: "))
b = int(input("Root number: "))

# some combinations doesn't return the correct result; be aware
# for testing, try these combinations: 25, 5; 8, 3; 1728, 3 (is 12)
print(f"Root of {base} by {b} is {root(base, b)}.")
