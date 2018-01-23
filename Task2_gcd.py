def gcd(x, y):
    if y == 0:
        return x
    if y > x:
        return gcd(y, x)

    return gcd(y, x % y)


print (gcd(10,15))