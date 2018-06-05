def digitDegree(n):
    result = 0
    n = str(n)
    
    while len(n) > 1:
        temp = 0
        for c in n:
            temp += int(c)
        
        n = str(temp)
        result += 1
        
    return result