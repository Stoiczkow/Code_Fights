import string

def isMAC48Address(inputString):
    splitted = inputString.split('-')
    allowed_vals = string.ascii_uppercase[0:6] + string.digits
    
    if len(splitted) != 6:
        return False
    
    for el in splitted:
        if len(el) != 2:
            return False
        
        if (el[0] in allowed_vals) and (el[1] in allowed_vals):
            pass
        else:
            return False
        
    return True
    
