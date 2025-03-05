txt = input(
)

words = txt.split('_')

print(words[0],end='')

for i in words:

    if i == words[0]:
        continue
    else:
        print(i[0].upper() + i[1:],end='')
