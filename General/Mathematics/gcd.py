# This is principal of Euclidean Algorithm
def gcd(a, b):
    if a > b:
        a = a-b
        gcd(a, b)
    elif b > a:
        b = b-a
        gcd(a, b)
    else:
        print(a)


gcd(26513, 32321)
