def deleteDigit(n):
    result = -1
    n_str = str(n)
    compare = ''
    
    for i in range(len(n_str)):
        compare = int(n_str[0:i]+n_str[i+1:])
        if compare > result:
            result = compare
    
    return result
