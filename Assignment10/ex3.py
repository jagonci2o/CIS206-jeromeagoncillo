import re

def aWithOneOrMoreB(word):
    result = bool(re.match("ab+", word))
    print(f"Does '{word}' have one or more B's: {result}")
    return result

aWithOneOrMoreB("ab")   
aWithOneOrMoreB("abc")  
aWithOneOrMoreB("a")  
aWithOneOrMoreB("ab")  
aWithOneOrMoreB("abb")
