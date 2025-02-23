import re

txt = input()

def to(text):
    return bool(re.fullmatch(r'a.*b', text))

print(to(txt))