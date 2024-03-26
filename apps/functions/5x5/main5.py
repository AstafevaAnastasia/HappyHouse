def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def check_win(board, player):
    for row in board:
        for i in range(2):
            if all([cell == player for cell in row[i:i + 4]]):
                return True

    for col in range(5):
        for i in range(2):
            if all([board[row][col] == player for row in range(i, i + 4)]):
                return True

    for i in range(2):
        if all([board[row][col] == player for row, col in zip(range(i, i + 4), range(i, i + 4))]):
            return True
        if all([board[row][col] == player for row, col in zip(range(i, i + 4), range(4, i - 5, -1))]):
            return True

    return False


board = [[' ' for _ in range(5)] for _ in range(5)]
players = ['X', 'O']
player_idx = 0

print_board(board)

for _ in range(25):
    row = int(input(f'Player {players[player_idx]}, enter row (1-5): ')) - 1
    col = int(input(f'Player {players[player_idx]}, enter column (1-5): ')) - 1

    if board[row][col] != ' ':
        print('Cell is already taken. Try again.')
        continue

    board[row][col] = players[player_idx]

    print_board(board)

    if check_win(board, players[player_idx]):
        print(f'Player {players[player_idx]} wins!')
        break

    player_idx = (player_idx + 1) % 2
else:
    print('It\'s a tie!')
