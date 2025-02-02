def spy_game(nums):
    num0 = 0
    num7 = 0
    for i in nums:
        if i == 0:
            num0+=1
        elif i == 7:
            num7+=1
    if num0 == 2 and num7 == 1:
        print(True)
    else:
        print(False)

l = [1, 2, 3, 4, 5, 6, 7]

y = [0, 0, 7]

spy_game(l)

spy_game(y)