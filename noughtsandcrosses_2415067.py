

import random
import os.path
import json
random.seed()

def draw_board(board):
    """
    Draw the unbeatable noughts and crosses board layout
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    

def welcome(board):
    """
   Displays a welcome message and the initial board layout.
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.\nThe board layout is show below:\n')
    draw_board(board)
    

def initialise_board(board):
    """
    Initializes an empty 3x3 Tic-Tac-Toe board.
    Returns:
        list: A 3x3 list filled with spaces representing empty cells.
    """
    board = []
    for _ in range(3):
        board.append([" "] * 3)
    return board

def get_player_move(board):
    """
    Prompts the player to enter their move.
    Ensures valid input and checks if the chosen cell is empty.
    
    Args:
        board: The current game board.
    
    Returns:
        tuple: chosen (row, column) coordinates.
    """
    while True:
        try:
            move = input("Enter your move (row and column seprated by space like (1 2)): ")
            row, col = map(int, move.split())
            if 1 <= row <= 3 and 1 <= col <= 3: 
                row, col = row -1, col -1 
                if board[row][col] == " ":
                    return row, col
                else:
                    print("Cell is occupied")
            else:
                print("Invalid move. Please try again")
        except ValueError:
           print("Invalid input")
    return row, col

def choose_computer_move(board):
    """
    Chooses a random move for the computer from available empty cells.
    
    Args:
        board: The current game board.
    
    Returns:
        tuple: The chosen (row, column) coordinates.
    """
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def check_for_win(board, mark):
    """
    Checks if the given mark ('X' or 'O') has won the game.
    
    Args:
        board: The current game board.
        mark: The player's or computer's mark ('X' or 'O').
    
    Returns:
        bool: True if the mark has won, False otherwise.
    """
    for i in range(3):
        if all([cell == mark for cell in board[i]]): 
            return True
        if all([board[j][i] == mark for j in range(3)]):  
            return True
    if all([board[i][i] == mark for i in range(3)]):  
        return True
    if all([board[i][2 - i] == mark for i in range(3)]):  
        return True
    return False

def check_for_draw(board):
    """
    Checks if the game has ended in a draw
    
    Args:
        board: The current game board.
    
    Returns:
        bool: True if the board is full, displays a draw.
    """

    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True
def play_game(board):
    """
    Runs the unbeatable noughts and crosses game loop.
    Alternates between the player and computer moves until there is a win or a draw.
    
    Returns:
        int: 1 if the player wins, -1 if the computer wins, 0 for a draw.
    """
    board = initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            print("Congrulations, You win!")
            return 1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

        row, col = choose_computer_move(board)
        board[row][col] = "O"
        print(f"Computer chooses: ({row + 1}, {col + 1})")
        draw_board(board)
        if check_for_win(board, "O"):
            print("Computer Wins!")
            return -1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

def menu():
    """
    Displays the game menu and prompts the user for a choice.
    
    Returns:
        str: The user's menu selection.
    """
    print("\nEnter one of the following options:")
    print("1 - Play the game")
    print("2 - Save your score in the leaderboard")
    print("3 - Load and display the leaderboard")
    print("q - End the program")
    
    while True:
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "q"]:
            return choice
        print("Invalid choice, Please try again")
    return choice
            
def load_scores():
    """
    Loads the leaderboard scores from 'leaderboard.txt'.
    
    Returns:
        dict: A dictionary of player names and their scores.
    """
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_score(score):
    """
    Saves the player's score in 'leaderboard.txt'.
    Updates the score if the player already exists.
    
    Args:
        score: The score to be saved.
    """
    name = input("Enter your name: ")
    leaders = load_scores()
    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(leaders, file)

def display_leaderboard(leaders):
    """
    Displays the leaderboard with player names and scores.
    
    Args:
        leaders: A dictionary containing player names and scores.
    """
    print("Leaderboard:")
    for name, score in leaders.items():
        print(f"{name}: {score}")