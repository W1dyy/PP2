import re

txt = input()

def to(text):
    return re.findall(r'\b[A-Z][a-z]+\b', text)

print(to(txt))
