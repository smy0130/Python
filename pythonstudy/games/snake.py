import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 색깔 정의
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 뱀과 먹이 초기 위치 설정
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (width//10)) * 10,
                 random.randrange(1, (height//10)) * 10]
food_spawn = True

# 이동 방향 초기 설정
direction = 'RIGHT'
change_to = direction

# 속도와 먹이를 먹을 때 꼬리 길이 증가 비율 설정
speed = 15
speed_multiplier = 0.8
tail_increase = 1

# 초기 score 설정
score = 0

# FPS 설정
fps = pygame.time.Clock()

# 게임 종료 함수
def game_over():
    global snake_position, snake_body, food_position, food_spawn, direction, change_to, speed, score
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is {}'.format(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width/2, height/4)
    screen.blit(game_over_surface, game_over_rect)

    # "Restart" 버튼 생성
    restart_button = pygame.Rect(width/2 - 70, height/2, 140, 50)
    pygame.draw.rect(screen, green, restart_button)
    restart_text = pygame.font.Font(None, 36).render("Restart", True, black)
    restart_text_rect = restart_text.get_rect(center=restart_button.center)
    screen.blit(restart_text, restart_text_rect)

    pygame.display.flip()

    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if restart_button.collidepoint(x, y):
                    snake_position = [100, 50]
                    snake_body = [[100, 50], [90, 50], [80, 50]]
                    food_position = [random.randrange(1, (width//10)) * 10,
                                     random.randrange(1, (height//10)) * 10]
                    food_spawn = True
                    direction = 'RIGHT'
                    change_to = direction
                    speed = 15
                    score = 0
                    waiting_for_restart = False

# 게임 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    if food_spawn:
        food_position = [random.randrange(1, (width//10)) * 10,
                         random.randrange(1, (height//10)) * 10]
    food_spawn = False

    new_head = [snake_position[0], snake_position[1]]

    if direction == 'RIGHT':
        new_head[0] += 10
    if direction == 'LEFT':
        new_head[0] -= 10
    if direction == 'UP':
        new_head[1] -= 10
    if direction == 'DOWN':
        new_head[1] += 10

    snake_body.insert(0, new_head)

    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        snake_body.append([0, 0])
        speed *= speed_multiplier
        food_spawn = True

    else:
        snake_body.pop()

    snake_position = new_head

    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    if snake_position[0] >= width or snake_position[0] <= 0:
        game_over()
    if snake_position[1] >= height or snake_position[1] <= 0:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    pygame.display.update()
    fps.tick(speed)