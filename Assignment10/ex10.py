import re

def modifyPhrase(phrase):
    print(f"Before: {phrase}")
    if ' ' in phrase:
        result = re.sub(r'\s+', '_', phrase)
    elif '_' in phrase:
        result = re.sub(r'_', ' ', phrase)
    else:
        result = phrase 
    return f"After: {result}"

print(modifyPhrase("Regular Expressions"))  
print(modifyPhrase("Code_Examples"))
