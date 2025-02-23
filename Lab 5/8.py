import re

txt = input()

def to(text):
    return re.findall(r'[^A-Z]*', text)[1:-1]


print(to(txt))