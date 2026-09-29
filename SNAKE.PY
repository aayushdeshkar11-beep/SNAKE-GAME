from mimetypes import init

import pygame
import random
import os
pygame.init()
pygame.mixer.init()



#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)


screen_width = 900
screen_height = 500
# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# title of game
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()



# game specific variables :--- as i wanted that the after the snake length increases if then tail of snake touches the head the game over by means the coordinates becomes equal the game overs
'''exit_game = False 
game_over = False

# variable value
snake_x = 100
snake_y = 100
snake_size = 20
velocity_x = 2
velocity_y = 1

food_x = random.randint(20,screen_width)
food_y = random.randint(20,screen_height)

score = 0
init_velocity = 5
fps = 40'''

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

#it is being linked with the 122 line of code
def plot_snake(gameWindow, color, snk_list, snake_size):
    #print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])



def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,220,229))
        text_screen('WELCOME TO SNAKES',black,260,250)
        text_screen('PRESS SPACE BAR TO PLAY', black, 232, 290)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    #GAME MUSIC STARTING MUSIC
                    pygame.mixer.music.load("short_orchestral.mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)

                    game_loop()


        pygame.display.update()
        clock.tick(40)


#Game loop logic of game is in this function as loops are implemnetd in it
def game_loop():
    # game specific variables
    exit_game = False
    game_over = False

    # variable value
    snake_x = 100
    snake_y = 100
    snake_size = 20
    velocity_x = 2
    velocity_y = 1

    food_x = random.randint(20, screen_width)
    food_y = random.randint(20, screen_height)

    score = 0
    init_velocity = 5
    fps = 40

    snk_list = []
    snk_length = 1

    # highscore program
    if not os.path.exists('highscore.txt'):
        with open('highscore.txt', 'w') as f:
            f.write(0)

    with open('high score.txt') as f:
        high_score = f.read()

    while not exit_game:
        if game_over:
            with open('high score.txt','w') as f:
                f.write(str(high_score))

            gameWindow.fill(white)
            text_screen('SAANP MAR GAYA chal phir se enter daba khelna hai toh', red,170, 150)

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        # IN THIS ELSE PART IF ANYBODY PRESSS THE KEY IT INIATED THE KEY SO THAT WE CAN USE THEM TO PLAY THE GAME
        else:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #snake_x = snake_x + 10
                        velocity_x =  init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        #snake_x = snake_x - 10
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        #snake_y = snake_y - 10
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        #snake_y = snake_y + 10
                        velocity_y = init_velocity
                        velocity_x = 0

                    #IT IS LIKE A CHEAT CODE KEY ISSME AGAR YE SIRF KEY PREESS KIYA TOH SCORE INCREASE HOJAYEGA
                    if event.key == pygame.K_q:
                        # BY JUST PRESSING THE Q THE VELOCITY GOES IN DOWNWARD DIRECTION
                        velocity_x = init_velocity
                        velocity_y = 2

                        score += 5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                #print('SCORE:',score*10) :-- not too much required as we are displaying from gamewindow.fill() func..

                food_x = random.randint(20,screen_width)
                food_y = random.randint(20,screen_height)
                snk_length +=4
                if score > int(high_score):
                    high_score = score



            gameWindow.fill(white)
            text_screen('SCORE:' + str(score) + '  highscore:' + str(high_score), green, 10, 10)
            pygame.draw.rect(gameWindow,red,[food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)

            snk_list.append(head)

            # imp part of this
            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

                pygame.mixer.music.load("game over.mp3")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

                pygame.mixer.music.load("game over.mp3")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)

            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
#game_loop() :--- why i commeneted this because as we have make another function for welcome i.e. def welome and in that we have introduces some text that appears on the screen so for that we wanted to print it and because gameloop is giving error while executing the window code we have just commeneted its return type