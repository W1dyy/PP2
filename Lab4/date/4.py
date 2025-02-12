import datetime 

x = datetime.datetime.now()

y = datetime.datetime.now().replace(minute=56)

if x > y:
    c = x-y

else:
    c = y-x

print(c)