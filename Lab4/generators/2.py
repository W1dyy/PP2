def gen(num):
    
    for i in range (0, num+1):
        if i%2==0:
            yield i

x = int(input())

y = gen(x)

for i in y:
    print(i, end=" ")
