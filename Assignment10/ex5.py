import re

text1 = "The quick brown fox jumps over the lazy dog."
text2 = " The quick brown fox jumps over the lazy dog."

def matchStart(sent1, sent2):
    firstWordsent1 = re.match(r"^\s*(\w+)", sent1)
    firstWordsent2 = re.match(r"^\s*(\w+)", sent2)
    
    if firstWordsent1 and firstWordsent2:
        if firstWordsent1.group(1) == firstWordsent2.group(1):
            print(f"The first words of each sentence match: '{firstWordsent1.group(1)}'")
            return True
        else:
            print("The first words of each sentence do not match.")
            return False
    return False

print(f'Sentence 1: "{text1}"\nSentence 2: "{text2}"')
print(matchStart(text1, text2))
