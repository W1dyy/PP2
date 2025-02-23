import re

txt = input()

def to(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


print(to(txt))