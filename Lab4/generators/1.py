def sqr(num):
    
    for x in range(num):
        yield x**2
        


x = int(input())

print(sqr(x))

