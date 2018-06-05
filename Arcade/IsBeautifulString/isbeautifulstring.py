import string

def isBeautifulString(inputString):
    counts = []    
    
    for char in string.ascii_lowercase:
        counts.append(inputString.count(char))
    
    for i in range(1, len(counts)):
        if counts[i] - counts[i-1] > 0:
            return False
    
    return True