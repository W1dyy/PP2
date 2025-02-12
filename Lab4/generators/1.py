def sqr(num):
    
    for x in range(1, num+1):
        yield x**2
        


x = int(input())

y = sqr(x)

for i in y:
    print(i)

