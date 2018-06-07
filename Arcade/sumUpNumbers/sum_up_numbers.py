import string

def sumUpNumbers(inputString):
    result = 0
    for punct in string.punctuation:
        inputString = inputString.replace(punct, ' ')
    
    splitted_str = inputString.split(' ')
    
    for i in splitted_str:
        if i.isdigit():
            result += int(i)
            
    return result
