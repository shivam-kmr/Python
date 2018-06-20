
def gcd(num1, num2):
    if num1 % num2 == 0:
        print(num2)

    for i in range(int(num2/2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            print(i)
            break


gcd(12, 8)