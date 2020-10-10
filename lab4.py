# Richard Waltiere rcw232@nau.edu
# Nick Persley 
import random

def main():
    board = [[False, True, True, True, True],       
            [True, True, True, True, True],           
            [True, True, True, True, True],          
            [True, True, True, True, True],    
            [True, True, True, True, True]] 
    
    print(not detect_on_off(board, 0, 0))


def lights_out():
    board = create_board()
    
    print_board(board) 
    
    while false_in_board(board):
        row = int(input("Please choose a row number(0-4): "))
        while not valid_row(row):
            print("That is not a valid row.")
            row = int(input("Please choose a row number(0-4): "))

        column = int(input("Please choose a column number (0-4): "))
        while not valid_column(column):
            print("That is not a valid column.")
            column = int(input("Please choose a column number(0-4): "))
        
        switch_lights(board, row, column)

        print_board(board)

def false_in_board(board):
    for i in range(5):
        if False in board[i]:
            return True
    
    return False

def valid_row(row):
    return row in range(5)

def valid_column(column):
    return column in range(5)

def print_board(board):
    display_board = [[], [], [], [], []]

    for row in range(5):
        for column in range(5):
            if board[row][column] == True:
                display_board[row].append("\N{WHITE SQUARE}")
            else:
                display_board[row].append("\N{BLACK SQUARE}")
       
    print("\n")
    
    for row in range(5):
        print("\t", row, "", *display_board[row], sep = '  ')
    
    column = [0, 1, 2, 3, 4] 
    print("\n", "\t", "   ", *column, sep = '  ')

    print("\n")
    
    return None

# Create a function that randomly generates and displays the board
# True signifies a light that is off, False a light that is on
def create_board():
    board = [[], [], [], [], []]
    
    for row in range(5): 
        for column in range(5):
            on_or_off = random.randint(0,1)
            
            if on_or_off == 0:
                board[row].append(True)
            else:
                board[row].append(False)


    return board
    

# Create a function which turns the appropriate lights on and off
def switch_lights(board, row, column):
    bool_list = test_row_column(row, column)
    
    if bool_list[0]:
        if bool_list[2]:
            board[0][0] = not detect_on_off(board, 0, 0)
            board[0][1] = not detect_on_off(board, 0, 1)
            board[1][0] = not detect_on_off(board, 1, 0)
 
        elif bool_list[3]:
            board[0][4] = not detect_on_off(board, 0, 4)
            board[0][3] = not detect_on_off(board, 0, 3)
            board[1][4] = not detect_on_off(board, 1, 4)
              
        else:
            board[0][column] = not detect_on_off(board, 0, column)
            board[0][column - 1] = not detect_on_off(board, 0, column - 1)
            board[0][column + 1] = not detect_on_off(board, 0, column + 1)
            board[1][column] = not detect_on_off(board, 1, column)
            
    elif bool_list[1]:
        if bool_list[2]:
            board[4][0] = not detect_on_off(board, 4, 0)
            board[4][1] = not detect_on_off(board, 4, 1)
            board[3][0] = not detect_on_off(board, 3, 0)
 
        elif bool_list[3]:
            board[4][4] = not detect_on_off(board, 4, 4)
            board[4][3] = not detect_on_off(board, 4, 3)
            board[3][4] = not detect_on_off(board, 3, 4)
              
        else:
            board[4][column] = not detect_on_off(board, 4, column)
            board[4][column - 1] = not detect_on_off(board, 4, column - 1)
            board[4][column + 1] = not detect_on_off(board, 4, column + 1)
            board[3][column] = not detect_on_off(board, 3, column)
    
    elif bool_list[2] and bool_list[0] == False and bool_list[1] == False:
        board[row][0] = not detect_on_off(board, row, 0)
        board[row - 1][0] = not detect_on_off(board, row - 1, 0)
        board[row + 1][0] = not detect_on_off(board, row + 1, 0)
        board[row][1] = not detect_on_off(board, row, 1)
    
    elif bool_list[3] and bool_list[0] == False and bool_list[1] == False:
        board[row][4] = not detect_on_off(board, row, 4)
        board[row - 1][4] = not detect_on_off(board, row - 1, 4)
        board[row + 1][4] = not detect_on_off(board, row + 1, 4)
        board[row][3] = not detect_on_off(board, row, 3)
    
    else:
        board[row][column] = not detect_on_off(board, row, column)
        board[row - 1][column] = not detect_on_off(board, row - 1, column)
        board[row + 1][column] = not detect_on_off(board, row + 1, column)
        board[row][column - 1] = not detect_on_off(board, row, column - 1)
        board[row][column + 1] = not detect_on_off(board, row, column + 1)

    
    
def detect_on_off(board, row, column):
    return board[row][column] == True
    
def test_row_column(row, column):
    bool_list = [False, False, False, False]
    if row == 0:
        bool_list[0] = True
    elif row == 4:
        bool_list[1] = True
    if column == 0:
        bool_list[2] = True
    elif column == 4:
        bool_list[3] = True

    return bool_list

    

# Create a function which tests a

lights_out()

