def sudoku(grid):
    for row in grid:
        for i in range(1, 10):
            if row.count(i) != 1:
                return False
        
    col = []
    for j in range(0, 9):
        for row in grid:
            col.append(row[j])
        
        if sum(col) != 45:
            return False
        col = []
    
    starters = [0, 3, 6]
        
    if (sum(grid[0][0:3])+sum(grid[1][0:3])+sum(grid[2][0:3])) != 45:
        return False
    
    if (sum(grid[3][0:3])+sum(grid[4][0:3])+sum(grid[5][0:3])) != 45:
        return False
    
    if (sum(grid[6][0:3])+sum(grid[7][0:3])+sum(grid[8][0:3])) != 45:
        return False
    
    if (sum(grid[0][3:6])+sum(grid[1][3:6])+sum(grid[2][3:6])) != 45:
        return False
    
    if (sum(grid[3][3:6])+sum(grid[4][3:6])+sum(grid[5][3:6])) != 45:
        return False
    
    if (sum(grid[6][3:6])+sum(grid[7][3:6])+sum(grid[8][3:6])) != 45:
        return False
    
    if (sum(grid[0][6:])+sum(grid[1][6:])+sum(grid[2][6:])) != 45:
        return False
    
    if (sum(grid[3][6:])+sum(grid[4][6:])+sum(grid[5][6:])) != 45:
        return False
    
    if (sum(grid[6][6:])+sum(grid[7][6:])+sum(grid[8][6:])) != 45:
        return False
        
    return True

