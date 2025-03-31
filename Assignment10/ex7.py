import re

def removeLeadZero(ip):
    print(f"Before removing leading zeros from an IP address: {ip}")  
    newIP = re.sub(r'\b0+(\d)', r'\1', ip)
    print(f"After removing leading zeros from an IP address: {newIP}")
    return newIP

removeLeadZero("216.08.094.196")
