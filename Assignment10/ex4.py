import re

def lowercaseWithUnderscore(phrase):
    result = bool(re.match("^[a-z]+_[a-z]+$", phrase))
    print(f'"{phrase}" sequence of lowercase letters joined by an underscore: {result}')
    return result

lowercaseWithUnderscore("aab_cbbbc")  
lowercaseWithUnderscore("aab_Abbbc")  
lowercaseWithUnderscore("Aaab_abbbc")
