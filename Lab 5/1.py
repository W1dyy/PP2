import re

txt = input()

def bs(text):
    return bool(re.fullmatch(r'ab*', text))


print(bs(txt))
