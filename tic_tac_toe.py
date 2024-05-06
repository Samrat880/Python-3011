import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LINE_COLOR = (0, 0, 0)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Board
board = [['' for _ in range(3)] for _ in range(3)]

# Fonts
font = pygame.font.Font(None, 80)

# Draw lines
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (WIDTH//3, 0), (WIDTH//3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH//3, 0), (2 * WIDTH//3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT//3), (WIDTH, HEIGHT//3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT//3), (WIDTH, 2 * HEIGHT//3), LINE_WIDTH)

# Draw X or O
def draw_XO(row, col):
    if board[row][col] == 'X':
        pygame.draw.line(screen, RED, (col * WIDTH//3 + WIDTH//10, row * HEIGHT//3 + HEIGHT//10), 
                         ((col + 1) * WIDTH//3 - WIDTH//10, (row + 1) * HEIGHT//3 - HEIGHT//10), LINE_WIDTH)
        pygame.draw.line(screen, RED, ((col + 1) * WIDTH//3 - WIDTH//10, row * HEIGHT//3 + HEIGHT//10), 
                         (col * WIDTH//3 + WIDTH//10, (row + 1) * HEIGHT//3 - HEIGHT//10), LINE_WIDTH)
    elif board[row][col] == 'O':
        pygame.draw.circle(screen, BLUE, (col * WIDTH//3 + WIDTH//6, row * HEIGHT//3 + HEIGHT//6), min(WIDTH//6, HEIGHT//6) - LINE_WIDTH)

# Check winner
def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

# Main loop
turn = 'X'
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            row = y // (HEIGHT // 3)
            col = x // (WIDTH // 3)
            if board[row][col] == '':
                board[row][col] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
    
    screen.fill(WHITE)
    draw_lines()
    for row in range(3):
        for col in range(3):
            draw_XO(row, col)
    
    winner = check_winner()
    if winner:
        game_over = True
        text = f"{winner} wins!"
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text_surface, text_rect)
    
    pygame.display.update()
