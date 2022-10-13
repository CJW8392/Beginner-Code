#Sets the matrix size to 9x9
M = 9

#Assign the function to print the grid
def puzzle(a):
    for r in range(M):
        for c in range(M):
            print(a[r][c],end = ",")
        print()

def solve(grid, row, col, num):
    #If the same number exists in the same row return False
    for x in range(9):
        if grid[row][x] == num:
            return False
    #If the same number exists in the same column return False         
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
## 0 means this is an empty square in the puzzle board
grid = [[0,6,0,0,9,0,0,1,0],
        [8,0,0,7,0,4,0,0,6],
        [0,0,1,0,0,0,2,0,0],
        [0,9,0,1,0,3,0,2,0],
        [4,0,0,0,0,0,0,0,7],
        [0,8,0,4,0,2,0,9,0],
        [0,0,7,0,0,0,8,0,0],
        [6,0,0,9,0,7,0,0,5],
        [0,4,0,0,3,0,0,7,0]] 

if (Suduko(grid, 0, 0)):
    puzzle(grid)

else:
    print("Solution does not exist:(")