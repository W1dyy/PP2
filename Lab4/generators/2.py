def gen(num):
    ls = []

    cnt = 2

    while cnt < num:
        ls.append(cnt)

        cnt+=2

    return ls

x = int(input())

y = gen(x)

print(y)