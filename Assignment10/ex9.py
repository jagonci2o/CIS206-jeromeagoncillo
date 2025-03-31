import re

text = 'The quick brown fox jumps over the lazy dog.'
keyword = 'fox'

def findWordAndLocation(text, word):
    pattern = re.escape(word)
    matches = [(m.start(), m.group()) for m in re.finditer(pattern, text)]
    if matches:
        position, wordFound = matches[0]
        return f"The word '{wordFound}' was found in position {position}."
    return f"The word '{word}' was not found."

print(text)

print(findWordAndLocation(text, keyword))
