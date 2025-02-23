import re

txt = input()

def to(text):
    return re.sub(r'[ ,.]', ':', text)

print(to(txt))