# This is a Tic-tac-toe game based on the terminal
#lst = [['X',' ',' '], [' ',' ',' '], [' ',' ',' ']]
def print_board(board):
    a = board[0][0]
    b = board[0][1]
    c = board[0][2]
    d = board[1][0]
    e = board[1][1]
    f = board[1][2]
    g = board[2][0]
    h = board[2][1]
    i = board[2][2]
    print(f'''
    ╔═══╦═══╦═══╗
    ║ {a} ║ {b} ║ {c} ║
    ╠═══╬═══╬═══╣
    ║ {d} ║ {e} ║ {f} ║
    ╠═══╬═══╬═══╣
    ║ {g} ║ {h} ║ {i} ║
    ╚═══╩═══╩═══╝
    ''')

def check_winner(board):
    # Define all possible winning combinations
    win_combinations = [
        # Rows
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Columns
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # Diagonals
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    # Check each winning combination
    for combo in win_combinations:
        positions = [board[r][c] for r, c in combo]
        if positions.count('X') == 3:
            return 'X'
        elif positions.count('O') == 3:
            return 'O'

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def start_new_game():
    new_board = [[' ' for _ in range(3)] for _ in range(3)]
    print('''
    ████████╗██╗ ██████╗      ████████╗ █████╗  ██████╗      ████████╗ ██████╗ ███████╗
    ╚══██╔══╝██║██╔════╝      ╚══██╔══╝██╔══██╗██╔════╝      ╚══██╔══╝██╔═══██╗██╔════╝
       ██║   ██║██║     █████╗   ██║   ███████║██║     █████╗   ██║   ██║   ██║█████╗  
       ██║   ██║██║     ╚════╝   ██║   ██╔══██║██║     ╚════╝   ██║   ██║   ██║██╔══╝  
       ██║   ██║╚██████╗         ██║   ██║  ██║╚██████╗         ██║   ╚██████╔╝███████╗
       ╚═╝   ╚═╝ ╚═════╝         ╚═╝   ╚═╝  ╚═╝ ╚═════╝         ╚═╝    ╚═════╝ ╚══════╝                                                                                                                                                                  
    ''')
    print("---------------------------------------------------------------------------------------")
    print("Welcome to Tic Tac Toe!")
    print("---------------------------------------------------------------------------------------")
    print("Here is the Rule:")
    print(
        "Tic-tac-toe is played on a three-by-three grid by two players. \nTwo players alternately place the marks X and O in one of the nine spaces in the grid. \nThe player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row first is the winner.")
    print("---------------------------------------------------------------------------------------")
    print("Here is a example grid with O and X mark")
    # this is a grid with O and X mark
    print('''
    ╔═══╦═══╦═══╗
    ║ O ║ O ║ O ║
    ╠═══╬═══╬═══╣
    ║ O ║ X ║ O ║
    ╠═══╬═══╬═══╣
    ║ O ║ O ║ O ║
    ╚═══╩═══╩═══╝
    ''')
    print("---------------------------------------------------------------------------------------")
    print("For playing the game, two players are needed!,")
    print("One player use the 'X' mark and the other one use the 'O' mark.")
    print("---------------------------------------------------------------------------------------")
    print_board(new_board)
    return new_board

def play_game():
    board = start_new_game()
    while not is_board_full(board):

        print("For player X (Enter number 1 - 3):")
        x_Hori = int(input("Please enter the number of the horizontal row you want to place the mark 'X' with:")) -1
        x_Vert = int(input("Please enter the number of the vertical row you want to place the mark 'X' with:")) -1
        board[x_Hori][x_Vert] = 'X'
        print_board(board)
        if check_winner(board) == 'X':
            print("You Win!")
            return "X!"

        print("For player O (Enter number 1 - 3 and press enter to continue):")
        o_Hori = int(input("Please enter the number of the horizontal row you want to place the mark 'O' with:")) -1
        o_Vert = int(input("Please enter the number of the vertical row you want to place the mark 'O' with:")) -1
        board[o_Hori][o_Vert] = 'O'
        print_board(board)
        if check_winner(board) == 'O':
            print("You Win!")
            return "O"
    return None


def main():
    winer = play_game()
    if winer is None:
        print("It's a tie!")
    else:
        print("Congratulations, " + winer + "!")

main()