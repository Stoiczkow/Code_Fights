import string

def chessKnight(cell):
    nums_col = {}
    num = 1
    result = 0
    for char in string.ascii_lowercase[:8]:
        nums_col[char] = num
        num +=1
    
    knight_position = (nums_col[cell[0]], int(cell[1]))
    
    possible_positions = [(2,1), (1,2), (-1, 2), (-2,1),
                          (-2,-1), (-1,-2), (1, -2), (2,-1)]
    
    for pos in possible_positions:
        if (knight_position[0] + pos[0] in range(1, 9)) and ((knight_position[1] + pos[1] in range(1, 9))):
            result += 1
            
    return result