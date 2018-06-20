numberofColor = int(input("Enter The Numbers of Color You Want "))
hello = []
for i in range(0, numberofColor):
    value = input("Color :")
    hello.append(value)

print(hello[0])
print(hello[-1])
