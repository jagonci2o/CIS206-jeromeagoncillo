import re

def checkString(input):  
    return bool(re.match("^[a-zA-Z0-9]+$", input))

print(checkString("ABCDEFabcdef123450")) 
print(checkString("*&%@#!}{"))             
