def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        
        # Entrée des coordonnées avec gestion des erreurs
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Vérification que les coordonnées sont valides
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid coordinates. Please enter values between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break  # Coordonnées valides, on peut sortir de la boucle
            except ValueError:
                print("Invalid input. Please enter integer values for row and column.")
        
        # Marquer le coup
        board[row][col] = player

        # Changer de joueur
        player = "O" if player == "X" else "X"
    
    print_board(board)
    print(f"Player {player} wins!")

tic_tac_toe()

