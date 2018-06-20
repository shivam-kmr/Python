def lcm(num1, num2):
    if num1 > num2:
        z = num1
    else:
        z = num2

    while(True):
        if((z % num1 == 0) and (z % num2 == 0)):
            ans = z
            break
        z = z + 1
    return ans

print(lcm(4, 6))

