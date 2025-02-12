def thr(num):
    
    for i in range (0, num+1):
        if i%3==0 and i%4==0:
            yield i

    


x = int(input())

y = thr(x)

for i in y:
    print(i, end=" ")
