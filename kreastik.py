def print_board(board):
    print("  0 1 2")
    for index, row in enumerate(board):
        print(f"{index} " + " ".join(row))

def check_winner(board, player):
    # Проверяем строки, столбцы и диагонали на наличие выигрыша
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    # Проверяем не наступила ли ничья
    return all(board[i][j] != '-' for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Добро пожаловать в игру Крестики-нолики!")
    print("Игрок 'X' ходит первым.")
    print("Для совершения хода введите номер строки и столбца через пробел (например, '1 2').")
    
    while True:
        print_board(board)
        print(f"Игрок {current_player}, ваш ход:")
        
        try:
            row, col = map(int, input().split())
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Номера строки и столбца должны быть от 0 до 2.")
                continue
            if board[row][col] != '-':
                print("Эта клетка уже занята. Выберите другую.")
                continue
            board[row][col] = current_player
        except ValueError:
            print("Некорректный ввод. Введите два числа от 0 до 2 через пробел.")
            continue
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break
        if check_draw(board):
            print_board(board)
            print("Ничья!")
            break
        
        # Меняем игрока после каждого хода
        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
