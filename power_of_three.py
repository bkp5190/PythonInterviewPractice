def powerOfThree(n: int):
    # Return True if the number is a power of three
    # if there exists x that n == 3^x
    while (n >= 3):
        if n % 3 != 0:
            return False
        n = n / 3
    return n == 1

assert powerOfThree(27) == True
assert powerOfThree(0) == False
assert powerOfThree(-1) == False
