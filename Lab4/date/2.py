import datetime 

x = datetime.datetime.now()

print("today is", x.year, '.', x.month, '.', x.day)

print("yesterday is", x.year, '.', x.month, '.', x.day-1)

print("tommorow is", x.year, '.', x.month, '.', x.day+1)