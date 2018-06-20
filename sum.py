def sum1(x, y, z):
    if x == y or y == z or x == z:
        add = 0
    else:
        add = x + y + z

    return add


print(sum1(3, 5, 10))