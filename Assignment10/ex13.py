import re

def replaceWithColon(phrase):
    updatedPhrase = re.sub(r'[ ,.]', ':', phrase)
    print("Before replacing all occurrences of a space, comma, or dot with a colon:", phrase)
    print("After replacing all occurrences of a space, comma, or dot with a colon:", updatedPhrase)
    return updatedPhrase

replaceWithColon('Python Exercises, PHP exercises.')  
