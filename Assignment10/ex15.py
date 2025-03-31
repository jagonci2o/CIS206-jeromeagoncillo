import re

text = 'Python      Exercises'

def removeMultipleSpaces(phrase):
    return re.sub(r'\s+', ' ', phrase).strip()

modifiedText = removeMultipleSpaces(text)

print(f'Before removing multiple spaces: {text}')
print(f'After removing multiple spaces: {modifiedText}')
