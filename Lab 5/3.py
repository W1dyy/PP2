import re

txt = input()

def to(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)

print(to(txt))