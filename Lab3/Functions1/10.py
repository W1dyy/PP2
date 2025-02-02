def unique_elem(list):
    x = []

    for i in list:       
        if i not in x:
            x.append(i)  

    return x


list = [1, 2, 3, 4, 5, 5, 6, 6, 8]

print(unique_elem(list))