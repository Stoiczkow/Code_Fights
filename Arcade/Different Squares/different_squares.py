def differentSquares(matrix):
    diff_squares = []
    current_square = []
    
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            try:
                current_square = (matrix[row][col],
                                  matrix[row][col+1],
                                  matrix[row+1][col],
                                  matrix[row+1][col+1])
                if current_square not in diff_squares:
                    diff_squares.append(current_square)
            except IndexError:
                pass
    
    return len(diff_squares)
            
