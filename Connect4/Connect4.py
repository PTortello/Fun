import math
import numpy as np
import pygame
import random
import sys

pygame.init()

def create_board():
    board = np.zeros((row_count, col_count))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_loc(board, col):
    return board[row_count - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def win_move(board, piece):
    # Check horizontals
    for c in range(col_count - 3):
        for r in range(row_count):
            if (board[r][c] == piece and board[r][c+1] == piece and
                board[r][c+2] == piece and board[r][c+3] == piece):
                return True
    
    # Check verticals
    for c in range(col_count):
        for r in range(row_count - 3):
            if (board[r][c] == piece and board[r+1][c] == piece and
                board[r+2][c] == piece and board[r+3][c] == piece):
                return True
    
    # Check positive diagonals
    for c in range(col_count - 3):
        for r in range(row_count - 3):
            if (board[r][c] == piece and board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and board[r+3][c+3] == piece):
                return True
    
    # Check negative diagonals
    for c in range(col_count - 3):
        for r in range(3, row_count):
            if (board[r][c] == piece and board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and board[r-3][c+3] == piece):
                return True

def draw_board(board):
    board = np.flip(board, 0)
    for c in range(col_count):
        for r in range(row_count):
            pygame.draw.rect(screen, blue, (c * square_size, r * square_size + square_size, square_size, square_size))
            if board[r][c] == 0:
                pygame.draw.circle(screen, black, (int(c * square_size + square_size / 2), int(r * square_size + square_size + square_size / 2)), radius)
            elif board[r][c] == player_piece:
                pygame.draw.circle(screen, red, (int(c * square_size + square_size / 2), int(r * square_size + square_size + square_size / 2)), radius)
            else:
                pygame.draw.circle(screen, yellow, (int(c * square_size + square_size / 2), int(r * square_size + square_size + square_size / 2)), radius)
    pygame.display.update()

def evaluate_window(window, piece):
    score = 0
    opp_piece = player_piece
    if piece == player_piece:
        opp_piece = ai_piece

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(empty) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(empty) == 2:
        score += 2
    if window.count(opp_piece) == 3 and window.count(empty) == 1:
        score -= 4
    return score

def score_position(board, piece):
    score = 0
    # Score center column
    center_array = [int(i) for i in list(board[:, col_count//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score horizontal
    for r in range(row_count):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(col_count - 3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Score vertical
    for c in range(col_count):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(row_count - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)
    
    # Score positive diagonal
    for r in range(row_count - 3):
        for c in range(col_count - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negative diagonal
    for r in range(row_count - 3):
        for c in range(col_count - 3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)
    return score

def is_terminal_node(board):
    return win_move(board, player_piece) or win_move(board, ai_piece) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if win_move(board, ai_piece):
                return (None, 1000000000000)
            elif win_move(board, player_piece):
                return (None, -1000000000000)
            else:   # Game is over, no more valid moves
                return (None, 0)
        else:   # Depth is zero
            return (None, score_position(board, ai_piece))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, ai_piece)
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:   # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, player_piece)
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

def get_valid_locations(board):
    valid_locations = []
    for col in range(col_count):
        if is_valid_loc(board, col):
            valid_locations.append(col)
    return valid_locations

def pick_best_move(board, piece):
    valid_locations = get_valid_locations(board)
    best_col = random.choice(valid_locations)
    best_score = -10000
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col

# Colors
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Screen
row_count = 6
col_count = 7
square_size = 100
radius = int(square_size / 2 - 5)
width = col_count * square_size
height = (row_count + 1) * square_size
screen = pygame.display.set_mode((width, height))
board = create_board()
# print_board(board)        # development purpose only
draw_board(board)
pygame.display.update()
myFont = pygame.font.SysFont("monospace", 75)

# Main game loop
_player = 0
_ai = 1
empty = 0
player_piece = 1
ai_piece = 2
gameover = False
turn = random.randint(_player, _ai)
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        # Player 1 as Human
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0, 0, width, square_size))
            posx = event.pos[0]
            pygame.draw.circle(screen, red, (posx, int(square_size / 2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0, 0, width, square_size))
            # Ask Player 1 input
            if turn == _player:
                posx = event.pos[0]
                col = int(math.floor(posx / square_size))
                if is_valid_loc(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, player_piece)
                    if win_move(board, player_piece):
                        label = myFont.render("Player 1 wins!", 1, red)
                        screen.blit(label, (40, 10))
                        gameover = True
                    # print_board(board)    # development purpose only
                    draw_board(board)                    
                    turn = (turn + 1) % 2

    # Player 1 as AI
    '''
    if turn == _player and not gameover:
        col = pick_best_move(board, player_piece)
        if is_valid_loc(board, col):
            pygame.time.wait(500)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, player_piece)
            if win_move(board, player_piece):
                label = myFont.render("Player 1 wins!", 1, red)
                screen.blit(label, (40, 10))
                gameover = True
            print_board(board)
            draw_board(board)
            turn = (turn + 1) % 2
    '''

    # Player 2 as AI
    if turn == _ai and not gameover:
        col = pick_best_move(board, ai_piece)                             # weak AI
        #col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)   # strong AI

        if is_valid_loc(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, ai_piece)
            if win_move(board, ai_piece):
                label = myFont.render("Player 2 wins!", 1, yellow)
                screen.blit(label, (40, 10))
                gameover = True
            # print_board(board)        # development purpose only
            draw_board(board)
            turn = (turn + 1) % 2

    if gameover:
        pygame.time.wait(3000)
