import PrintBoard
import CheckWin

board = [[' ' for _ in range(5)] for _ in range(5)]
players = ['❌', '⭕']
player_idx = 0

PrintBoard.print_board(board)

for _ in range(25):
    row = int(input(f'Player {players[player_idx]}, enter row (1-5): ')) - 1
    col = int(input(f'Player {players[player_idx]}, enter column (1-5): ')) - 1

    if board[row][col] != ' ':
        print('Cell is already taken. Try again.')
        continue

    board[row][col] = players[player_idx]

    PrintBoard.print_board(board)

    if CheckWin.check_win(board, players[player_idx]):
        print(f'Player {players[player_idx]} wins!')
        break

    player_idx = (player_idx + 1) % 2
else:
    print('It\'s a tie!')
