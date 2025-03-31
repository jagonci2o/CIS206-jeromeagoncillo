import re

text1 = "The quick brown fox jumps over the lazy dog."
text2 = "Python Exercises."

def zWord(text):
    if re.search(r"\w*z\w*", text):
        return f'The sentence, "{text}" contains "z".'
    else:
        return f'The sentence, "{text}" does not contain "z".'

print(zWord(text1)) 
print(zWord(text2))
