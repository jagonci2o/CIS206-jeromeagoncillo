import re

text = 'The quick brown fox jumps over the lazy dog.'

findWords = ['fox', 'dog', 'horse']

print(text)

for word in findWords:
    if re.search(r'\b' + re.escape(word) + r'\b', text):
        print(f"The word, '{word}', was found in the text.")
    else:
        print(f"The word,'{word}', was not found in the text.")
