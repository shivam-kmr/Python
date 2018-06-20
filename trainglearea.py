def trianglearea(base, height):
    return 0.5 * base * height


userbase = int(input("Enter The Base of Triangle"))
userheight = int(input("Enter The Height of Triangle"))

ans = trianglearea(userbase,userheight)
print(ans)