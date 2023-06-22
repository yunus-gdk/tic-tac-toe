# Your task is to write a simple program which pretends to play tic-tac-toe with the user.
# To make it all easier for you, we've decided to simplify the game. Here are our assumptions:
# the computer (i.e., your program) should play the game using 'X's;
# the user (e.g., you) should play the game using 'O's;
# the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
# all the squares are numbered row by row starting with 1 (see the example session below for reference)
# the user inputs their move by entering the number of the square they choose − 
# the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
# the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
# the computer responds with its move and the check is repeated;
# don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.
import random
import sys

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
        ]

def display_board(board):
    # The function accepts one parameter containing the board's current status and prints it out to the console.
    print(f"+-------+-------+-------+")
    for row in range(len(board)):
        print(f"|       |       |       |")
        for column in range(len(board[row])):
            print(f"|   {board[row][column]}   ", end = "")
        print(f"\n|       |       |       |\n+-------+-------+-------+")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; the list consists of tuples, while each tuple is a pair of row and column numbers.
    board_value = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            board_value += [ i for i in board[row][column] if ((i != "X") and (i != "O")) ]
    return board_value

def make_choice(choice, value):
    for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == choice:
                    board[row][column] = value

def board_value_empty(board_value):
    if not board_value: 
        print("NO WINNER !!!")
        sys.exit()

def enter_move(board_value):
    board_value_empty(board_value)

    while True:
        choice = input("Enter your move: ")

        if choice not in make_list_of_free_fields(board_value):
            print("Please choose a valid option: ")
            display_board(board)
            continue
        
        make_choice(choice, value="O")
        break

def draw_move(board_value):
    # The function draws the computer's move and updates the board.
    board_value_empty(board_value)

    choice = random.choice(make_list_of_free_fields(board_value))
    print(f"Computer's move: {choice}")

    make_choice(choice, value="X")

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if the player using 'O's or 'X's has won the game
    if board[0][0] == board[0][1] == board[0][2]: 
        print(f"{sign} wins !!!")
        sys.exit()
    if board[1][0] == board[1][1] == board[1][2]: 
        print(f"{sign} wins !!!")
        sys.exit()
    if board[2][0] == board[2][1] == board[2][2]: 
        print(f"{sign} wins !!!")
        sys.exit()
    if board[0][0] == board[1][0] == board[2][0]: 
        print(f"{sign} wins !!!")
        sys.exit()
    if board[0][1] == board[1][1] == board[2][1]: 
        print(f"{sign} wins !!!")
        sys.exit()
    if board[0][2] == board[1][2] == board[2][2]: 
        print(f"{sign} wins !!!")
        sys.exit()
    if board[0][0] == board[1][1] == board[2][2]: 
        print(f"{sign} wins !!!")
        sys.exit()
    if board[0][2] == board[1][1] == board[2][0]: 
        print(f"{sign} wins !!!")
        sys.exit()        

display_board(board)
while True:
    draw_move(make_list_of_free_fields(board))
    display_board(board)
    victory_for(board, sign="Computer")
    enter_move(make_list_of_free_fields(board))
    display_board(board)
    victory_for(board, sign="User")