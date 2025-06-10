# This is a Tic-tac-toe Terminal Game
def print_board(board):
    # prints the board
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
    print("--------------------------------------------------------------------------------اريات")
    show_position_guide()
    print_board(new_board)
    return new_board

def play_game():
    board = start_new_game()
    current_player = 'X'
    
    while True:
        # Get valid move
        while True:
            row, col = get_valid_input(current_player)
            if is_position_empty(board, row, col):
                board[row][col] = current_player
                break
            else:
                print("That position is already taken! Try again.")
        
        print_board(board)
        
        # Check for the winner
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins! 🎉")
            return winner
        
        # Check for tie
        if is_board_full(board):
            print("It's a tie! 🤝")
            return None
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

def get_valid_input(player_mark):
    """Get valid row and column input from the player"""
    while True:
        try:
            print(f"For player {player_mark} (Enter number 1 - 3):")
            row = int(input(f"Please enter the horizontal row for '{player_mark}': ")) - 1
            col = int(input(f"Please enter the vertical column for '{player_mark}': ")) - 1
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Please enter numbers between 1 and 3!")
        except ValueError:
            print("Please enter valid numbers!")

def is_position_empty(board, row, col):
    """Check if the position is empty"""
    return board[row][col] == ' '

def show_position_guide():
    """Show a position reference guide for the players"""
    print("Position guide (row, column):")
    print("╔═══╦═══╦═══╗")
    print("║1,1║1,2║1,3║")
    print("╠═══╬═══╬═══╣")
    print("║2,1║2,2║2,3║")
    print("╠═══╬═══╬═══╣")
    print("║3,1║3,2║3,3║")
    print("╚═══╩═══╩═══╝")


def main():
    while True:
        winner = play_game()
        
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing! 👋")
            break

main()

# Main improve of the 1.2 version:

### 1. **Input Validation and Error Handling**

### 3. **Better Game Flow Logic**

### 4. **Add Position Reference Guide**

### 5. **Add Replay Functionality**
