import re
# Questions 12 and 14 are the same

sentences = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

def findWordsStartingWithAOrE(finds):
    pattern = r'\b[aAeE]\w*'
    words = re.findall(pattern, finds)
    print("Here are the words that start with 'a' or 'e' in the sentences:")
    return words

print("Here is the prompt: " + sentences)
print(findWordsStartingWithAOrE(sentences))
