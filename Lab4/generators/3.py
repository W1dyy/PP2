def thr(num):
    
    ls = []

    cnt = 0

    while cnt < num:
        if cnt%3==0 and cnt%4==0:
            ls.append(cnt)
        cnt+=1

    return ls


x = int(input())


print(thr(x))