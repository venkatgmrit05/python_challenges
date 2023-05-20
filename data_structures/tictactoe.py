# non oops

import numpy as np


def iseven(n):
    return n % 2 == 0


def isodd(n):
    return n % 2 != 0


def replace_with(a: list, n, s):

    a.insert(n, s)
    a.remove(n)
    return a

# initializing board


def get_board_repr(board):
    r, c = board.shape
    board_str = ''
    board_strs = []
    for i in range(r):
        r_str = ' '.join(board[i, :])
        board_strs.append(r_str)
        # print(r_str)

    board_str = '\n'.join(board_strs)
    return board_str


def get_player_symbol(symbol):

    if symbol.strip() == "X":
        return '1'
    else:
        return '2'


def check_win_condition(ret):
    win_symbol = None
    winner = None
    if len(ret) == 1:
        win_symbol = list(ret)[0]
        winner = get_player_symbol(win_symbol)
        return winner
    return winner


def get_winner(board):

    winner = None
    r, c = board.shape

    # check rows
    for i in range(r):
        ret = set(board[i, :])
        winner = check_win_condition(ret)
        if winner:
            return winner

    # check columns
    for i in range(c):
        ret = set(board[:, i])
        winner = check_win_condition(ret)
        if winner:
            return winner

    # check diagonals
    ret = board.diagonal()
    winner = check_win_condition(ret)
    if winner:
        return winner

    ret = np.fliplr(board).diagonal()
    winner = check_win_condition(ret)
    if winner:
        return winner

    return winner


def get_board(board_values, board_shape: str = 'square'):

    board_values = [str(i).rjust(4) for i in board_values]

    num_grid = len(board_values)
    board_type = 'square'
    if board_type == 'square':
        board_shape = int(np.sqrt(num_grid))
    r, c = (board_shape, board_shape)
    a = np.array(board_values).reshape(r, c)
    a = a.astype(str)

    return a


if __name__ == '__main__':

    player_sym = {
        'player0': 'X',
        'player1': 'O'
    }

    num_values = 9
    board_values = list(range(num_values))

    termination_limit = 20
    i = 0

    players = [input('enter name'), input('enter name')]
    print(players)

    winner = None
    if i <= termination_limit:

        while winner is None:
            i += 1
            if isodd(i):
                player = players[0]
            else:
                player = players[1]

            user_input = input(f"enter grid num {player} : ")
            board_values = replace_with(
                board_values, int(user_input),
                player_sym[f"player{players.index(player)}"],
            )
            board = get_board(board_values)
            board_str = get_board_repr(board)
            winner = get_winner(board)
            print('\n\n')
            print(board_str)
            if winner:
                print(f'winner: {player}')
                break
