import datetime 

a = input()

b = input()

format = "%Y-%m-%d %H:%M:%S"

x = datetime.strptime(a, format)
y = datetime.strptime(b, format)

if x > y:
    c = x-y

else:
    c = y-x

print(c.total_seconds())
