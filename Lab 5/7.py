import re

txt = input()



def to(text):
    return ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(text.split('_')))


print(to(txt))