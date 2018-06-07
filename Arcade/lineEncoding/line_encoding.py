def lineEncoding(s):
    current = s[0]
    to_add = s[0]
    splitted = []
    for i in range(1, len(s)):
        if s[i] == current:
            to_add += s[i]
        else:
            if len(to_add) > 1:
                splitted.append(str(len(to_add)) + current)
            else:
                splitted.append(current)
            current = s[i]
            to_add = s[i]
            
    if len(to_add) > 1:
        splitted.append(str(len(to_add)) + current)
    else:
        splitted.append(current)
                
    return ''.join(splitted)
