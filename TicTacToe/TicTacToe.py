"""
Author:         Ethan Smith
Date:           October 26th 2023
Assignment:     TicTacToe Project
Course:         CPSC1050
Section:        F23

CODE DESCRIPTION:
This code plays a simple game of TicTacToe. The code alternates between two players
to place their respective piece, X or O, onto an intially empty 2D board. After
each turn the game will check if there is a winner. After announcing the results the
game will then ask if they would like to play again.

"""
def ex_board():
    """ Creates the example board for the introduction

    Return:
        Example board layout
    """
    return [['', '', 'X'], ['', '', ''], ['', '', '']]

def init_board():
    """Sets the initial board that is set to update after every turn

    Return:
        Empty board
    """
    return [['', '', ''], ['', '', ''], ['', '', '']]

def print_board(board):
    """Creates the layout of the 2D array, forming it into a 3x3 box separated by | and spaced by ' _ '

    Args:
        board: Nested list of spaces, X's, and/or O's
    """
    output_string = ""
    for row in board:
        output_string += "|"
        for col in row:
            if col != "":
                output_string += f" {col} |"
            else:
                output_string += f" _ |"
        output_string += "\n"
    print(output_string)

def update_board(board, row, col, player):
    """Updates the board after every turn, replacing the empty space with an X or O

    Args:
        board: Nested list of spaces, X's, and/or O's
        row: Row of spaces
        col: Column of spaces
        player: The current player, X or O depending on whose turn it is
    """
    if board[row][col] == "": # If the space is empty, replace with X or O
        board[row][col] = player

def get_move(player):
    """Collects player information on where they would like to place their piece

    Args:
        player: The current player, X or O depending on whose turn it is

    Return:
        row: Returns what row they've chosen
        col: Returns what column they've chosen
    """
    # Sets the default prompt to be displayed
    prompt = f"Enter row and column for player {player}\n"

    while True:
        user_input = input(prompt).split() #Collects the input for the prompt

        try:
            row, col = map(int, user_input) # Potential ValueError and IndexError
            if 1 <= row <= 3 and 1 <= col <= 3: # If row and col is 1 to 3
                return row, col
            else:
                prompt = "Please enter valid row and col numbers from 1 to 3:\n" # Changes the prompt then repeats the loop

        except (ValueError, IndexError):
            prompt = "Please enter valid row and col numbers from 1 to 3:\n"
            pass

def player_move(board, player):
    """Finalizes the move and updates the board, checks if spot is already occupied first

    Args:
        board: Nested list of spaces, X's, and/or O's
        player: The current player, X or O depending on whose turn it is
    """
    while True:
        row, col = get_move(player)
        if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == "":
            update_board(board, row - 1, col - 1, player)
            break
        else:
            print("That spot is full!")

def check_for_win(board, player):
    """Checks the entire board for a diagonal, horizontal, or vertical win

    Args:
        board: Nested list of spaces, X's, and/or O's
        player: The current player, X or O depending on whose turn it is

    Return:
        bool: True of the player has achieved a win, False otherwise.
    """
    for i in range(3): # Checks for horizonal or vertical win
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    #Checks for diagonal win
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_for_tie(board):
    """Checks the entire board for a tie condition

    Args:
        board: Nested list of spaces, X's, and/or O's

    Return:
        bool: True of the player has achieved a win, False otherwise.
    """
    return all(board[i][j] != '' for i in range(3) for j in range(3))

def start_game():
    """Prints out the introduction and states who goes first
    """
    print("Let's play Tic-Tac-Toe!")
    print("When prompted, enter desired row and column numbers")
    print("Example: 1 3\n")
    board = ex_board()
    print_board(board)
    print("Let's play!")
    print("Player X starts!\n")

def play_again():
    """Asks the user if they would like to play their TicTacToe game again or not

    Validates whether or not if the user has inputted the correct response, 
    case-insensitive and ignores whitespace
    """
    YN = input("Do you want to play again? Y or N\n").upper().strip()

    if YN == 'Y': # Restarts the game
        play()
    
    elif YN == 'N':
        pass

    while not (YN == 'Y' or YN == 'N'): # Input Validation
        print("Please enter valid input: Y or N")
        YN = input("Do you want to play again? Y or N\n").upper().strip()
        if YN == 'Y': # Restarts the game
            play()

def play():
    """Kicks off the game and calls each function necessary.

    Prints out the results of the game and swaps players after each turn
    """
    board = init_board()
    current_player = 'X'

    start_game()
    
    while True:
        print_board(board)

        player_move(board, current_player)

        if check_for_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            play_again()
            break
        elif check_for_tie(board):
            print_board(board)
            print("It's a tie!")
            play_again()
            break
        
        current_player = 'O' if current_player == 'X' else 'X' # Swaps player

play()