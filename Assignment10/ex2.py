import re

def aWithNoneOrMoreB(word):
    result = bool(re.match("ab*", word))
    print(f"Does '{word}' have none or more B's: {result}")
    return result

aWithNoneOrMoreB("ab")   
aWithNoneOrMoreB("abc")  
aWithNoneOrMoreB("a")  
aWithNoneOrMoreB("ab")  
aWithNoneOrMoreB("abb")
