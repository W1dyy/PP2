def squares(num, num1):
    for i in range (num, num1 + 1):
        yield i**2


x = int(input())

z = int(input())

if x < z:

    y = squares(x, z)

else:
    y = squares(z, x)


for i in y:
    print(i, end=" ")
