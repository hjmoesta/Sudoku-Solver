board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def print_sud_board(board):
    ## pretty formatting in order to print the board out given the board ##
    for x in range(len(board)):
        if x % 3 ==0 and x != 0:
            print("- - - - - - - - - - - - ")
        for y in range(len(board[0])):
            if y % 3 ==0 and y != 0 :
                print(" | ", end="")
            if y == 8:
                print(board[x][y])
            else:
                print(str(board[x][y]) + " ", end="")

def find_zero(board):
    ## finds the 0 (empty value) on the board and returns the (x,y) value of the 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                return (x,y)
    return None

def valid_placement(board, position, num):
    #Check row
    for x in range(len(board[0])):
        if board[position[0]][x] == num and position[1] != x:
            return False

    # Check column
    for x in range(len(board)):
        if board[x][position[1]] == num and position[0] != x:
            return False

    # Check box
    x_box= position[1] // 3
    y_box = position[0] // 3

    for i in range(y_box*3, y_box*3 + 3):
        for j in range(x_box * 3, x_box*3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False
    return True

def solve_board(board):
    loc = find_zero(board)
    if not loc:
        return True
    x,y = loc
    for num in range(1,10):
       if valid_placement(board,(x,y),num):
           board[x][y] = num
           if solve_board(board):
               return True
           board[x][y] = 0 
    return False

print_sud_board(board)
solve_board(board)
print("___________________")
print_sud_board(board)
