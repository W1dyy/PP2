import re

txt = input()

def to(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)


print(to(txt))