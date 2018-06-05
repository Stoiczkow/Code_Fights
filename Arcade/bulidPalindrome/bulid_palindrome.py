def buildPalindrome(st):
    to_add = ''
    num = 0
    st_to_compare = st
    while st_to_compare != st_to_compare[::-1]:
        to_add = st[num] + to_add
        st_to_compare = st + to_add
        num += 1
    
    return st_to_compare