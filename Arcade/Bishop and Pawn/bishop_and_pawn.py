import string

def bishopAndPawn(bishop, pawn):
    rows_diff = abs(int(bishop[1]) - int(pawn[1]))
    nums_col = {}
    num = 1
    for char in string.ascii_lowercase[:8]:
        nums_col[char] = num
        num +=1
    
    if abs(nums_col[pawn[0]] - nums_col[bishop[0]]) == rows_diff:
        return True
    else:
        return False
