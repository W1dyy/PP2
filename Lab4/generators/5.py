def down(num):
    for i in range(num, -1, -1):
        yield i

x = int(input())

if x <= 0:
    print("error")
    

else:
    y = down(x)

    for i in y:
        print(i, end=" ")