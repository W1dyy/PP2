import re

def match_pattern(text): 
    match = re.fullmatch(r'ab{2,3}', text) 
    return bool(match)


test_strings = input()

print(match_pattern(test_strings))
