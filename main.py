from random import randint, random, randrange, choice
import pygame, math, os
pygame.init()



WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (128,128,128)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pyPong")
SCORE_1, SCORE_2 = 0, 0
ICON = pygame.image.load('icon.png')
pygame.display.set_icon(ICON)

font = pygame.font.Font('freesansbold.ttf', 64)


def draw(player_1 = None, player_2 = None, ball_x = None, ball_y = None):
    WIN.fill(BLACK)
    txt = "{} : {}".format(SCORE_1, SCORE_2)
    text = font.render(txt, True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (400, 200)

    WIN.blit(text, textRect)
    pygame.draw.circle(WIN, RED, (ball_x, ball_y), 10)
    pygame.draw.rect(WIN, BLUE, (20, player_1, 25, 100))
    pygame.draw.rect(WIN, BLUE, (WIDTH - 40, player_2, 25, 100))
    pygame.display.update()

def main():
    global SCORE_1, SCORE_2
    SPEED = 0.1
    BALL_SPEED = SPEED - 0.03
    countdown = 1
    ball_direction = choice([i for i in range(1, 8) if i not in[1, 5]])
    ball_x = randint(350, 450)
    ball_y = randint(150, 250)
    player_1, player_2 = 100, 100
    player_1_up, player_2_up = False, False
    player_1_down, player_2_down = False, False
    RUN = True    
    while RUN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            print(ball_x, ball_y)
            print(player_1)
        if keys[pygame.K_DOWN]:
            player_2_up = True
        if keys[pygame.K_UP]:
            player_2_down = True
        if keys[pygame.K_w]:
            player_1_up = True
        if keys[pygame.K_s]:
            player_1_down = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
            if event.type == pygame.KEYUP:
                player_1_down = False
                player_1_up = False
                player_2_down = False
                player_2_up = False 
        if player_1_up: player_1 -= SPEED
        elif player_1_down: player_1 += SPEED
        if player_2_up: player_2 += SPEED
        elif player_2_down: player_2 -= SPEED
        if ball_direction == 2:
            ball_x += BALL_SPEED
            ball_y -= BALL_SPEED
        elif ball_direction == 3: ball_x += BALL_SPEED
        elif ball_direction == 4:
            ball_x += BALL_SPEED
            ball_y += BALL_SPEED
        elif ball_direction == 6:
            ball_x -= BALL_SPEED
            ball_y += BALL_SPEED
        elif ball_direction == 7: ball_x -= BALL_SPEED
        elif ball_direction == 8:
            ball_x -= BALL_SPEED
            ball_y -= BALL_SPEED
        if player_1_up == False and player_1_down == False and math.floor(ball_x) == 55 and ball_y  >= player_1 and ball_y <= player_1 + 110:
            if ball_direction == 6: ball_direction = 4
            elif ball_direction == 7: ball_direction = 3
            elif ball_direction == 8: ball_direction = 2
            BALL_SPEED += BALL_SPEED * (5 / 100)

        elif player_1_up == True and math.floor(ball_x) == 55 and ball_y >= player_1 and ball_y <= player_1 + 110:
            if ball_direction == 6: ball_direction = 3
            elif ball_direction == 7: ball_direction = 2
            elif ball_direction == 8: ball_direction = 2
            BALL_SPEED += BALL_SPEED * (5 / 100)
        elif player_1_down == True and math.floor(ball_x) == 55 and ball_y >= player_1 and ball_y <= player_1 + 110:
            if ball_direction == 6: ball_direction = 4
            elif ball_direction == 7: ball_direction = 4
            elif ball_direction == 8: ball_direction = 3
            BALL_SPEED += BALL_SPEED * (5 / 100)
        if player_2_up == False and player_2_down == False and math.floor(ball_x) == WIDTH - 40 + 10 - 20 and ball_y >= player_2 and ball_y <= player_2 + 110:
            if ball_direction == 2: ball_direction = 8
            if ball_direction == 3: ball_direction = 7
            if ball_direction == 4: ball_direction = 6
            BALL_SPEED += BALL_SPEED * (5 / 100)
        if player_2_down == True and math.floor(ball_x) == WIDTH - 40 + 10 - 20 and ball_y >= player_2 and ball_y <= player_2 + 110:
            if ball_direction == 4: ball_direction = 7
            elif ball_direction == 3: ball_direction = 8
            elif ball_direction == 2: ball_direction = 8
            BALL_SPEED += BALL_SPEED * (5 / 100)
        if player_2_up == True and math.floor(ball_x) == WIDTH - 40 + 10 - 20 and ball_y >= player_2 and ball_y <= player_2 + 110:
            if ball_direction == 4: ball_direction = 6
            elif ball_direction == 3: ball_direction = 6
            elif ball_direction == 2: ball_direction = 7
            BALL_SPEED += BALL_SPEED * (5 / 100)
        if math.floor(ball_y) == 0:
            if ball_direction == 8: ball_direction = 6
            elif ball_direction == 2: ball_direction = 4
        if math.floor(ball_y) == HEIGHT:
            if ball_direction == 6: ball_direction = 8
            elif ball_direction == 4: ball_direction = 2
        if math.floor(ball_x) == 0:
            SCORE_2 += 1
            main()
        if math.floor(ball_x) == WIDTH:
            SCORE_1 += 1
            main()
        draw(player_1, player_2, ball_x, ball_y)







if __name__ == '__main__':
    main()