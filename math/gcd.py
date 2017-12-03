def gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    if x > y:
        temp = y
        y = x
        x = temp
    c = 1
    while c > 0:
        c = y % x
        y = x
        x = c
    return y

print(gcd(15,25))
