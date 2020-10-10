# Richard Waltiere rcw232@nau.edu
# Nick Persley 
import random

def main():
    board = [[False, True, True, True, True],                                                                         [True, True, True, True, True],                                                                         [True, True, True, True, True],                                                                         [True, True, True, True, True],                                                                         [True, True, True, True, True]] 
    
    print(not detect_on_off(board, 0, 0))


def lights_out():
    row = input("Please choose a row number(0-4): ")
    column = input("Please choose a column number (0-4): ") 


# Create a function that randomly generates and displays the board
def create_board():
    board = [[True, True, True, True, True], 
             [True, True, True, True, True], 
             [True, True, True, True, True],
             [True, True, True, True, True], 
             [True, True, True, True, True]]
    

    for row in range(5):
        for column in range(5):
            on_or_off = random.randint(0,1)
            
            if on_or_off == 0:
                board[row][column] = True
            else:
                board[row][column] = False

    return board
    

# Create a function which turns the appropriate lights on and off
def switch_lights(board, row, column):
    bool_list = test_row_column(row, column)
    
    if bool_list[0]:
        if bool_list[2]:
            board[0][0] = not detect_on_off(board, 0, 0)
            board[0][1] = not detect_on_off(board, 0, 1)
            board[1][0] = not detect_on_off(board, 0, 2)
 
        elif bool_list[3]:
            board[0][4] = not detect_on_off(board, 0, 1)
            board[0][3] = not detect_on_off(board, 0, 1)
            board[1][4] = not detect_on_off(board, 0, 1)
              
        else:
            pass

    
    
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

main()

