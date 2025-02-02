def histogram(list):
    for i in list:
        x = 0
        while x < i:
            print('*', end="")
            x+=1
        print(" ")

list = [1, 2, 3]

histogram(list)