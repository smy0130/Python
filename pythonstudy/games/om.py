'''
Created on 2023. 8. 17.

@author: 유승민
'''
import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 크기 설정
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Omok Game")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)

# 오목 판 설정
cell_size = 40
board_size = 15
board_offset = (width - cell_size * (board_size - 1)) // 2
board = [[0] * board_size for _ in range(board_size)]

# 플레이어 설정
current_player = 1

# 게임 종료 함수
def game_over(winner):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Player {winner} wins!", True, white)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

# 컴퓨터 AI
def computer_move():
    while True:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if board[row][col] == 0:
            return row, col

# 승리 조건 체크
def check_winner(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for dr, dc in directions:
        count = 1
        for i in range(1, 5):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < board_size and 0 <= c < board_size and board[r][c] == current_player:
                count += 1
            else:
                break
        
        for i in range(1, 5):
            r, c = row - dr * i, col - dc * i
            if 0 <= r < board_size and 0 <= c < board_size and board[r][c] == current_player:
                count += 1
            else:
                break

        if count >= 5:
            return True
    return False

# 게임 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and current_player == 1:
            mouse_x, mouse_y = event.pos
            col = (mouse_x - board_offset + cell_size // 2) // cell_size
            row = (mouse_y - board_offset + cell_size // 2) // cell_size
            if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == 0:
                board[row][col] = current_player
                if check_winner(row, col):
                    game_over(current_player)
                else:
                    current_player = 2

                if current_player == 2:
                    computer_row, computer_col = computer_move()
                    board[computer_row][computer_col] = current_player
                    if check_winner(computer_row, computer_col):
                        game_over(current_player)
                    else:
                        current_player = 1

    screen.fill(black)

    # 오목 판 그리기
    for row in range(board_size):
        for col in range(board_size):
            pygame.draw.rect(screen, white, pygame.Rect(board_offset + col * cell_size, board_offset + row * cell_size, cell_size, cell_size), 1)
            if board[row][col] == 1:
                pygame.draw.circle(screen, white, (board_offset + col * cell_size, board_offset + row * cell_size), cell_size // 2 - 2)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, white, (board_offset + col * cell_size, board_offset + row * cell_size), cell_size // 2 - 2, 1)

    pygame.display.flip()

# 게임 종료
pygame.quit()