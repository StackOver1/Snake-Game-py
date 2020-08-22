import random
import pygame
pygame.init()

# Colors
white = (225, 255, 255)
cyan = (0, 200, 255)
red = (255, 0, 0)
tomato = (255, 0, 150)

# Creating window
screen_width = 900
screen_height = 600
hiscore = 0
gameWindow = pygame.display.set_mode((screen_width, screen_height))
bgimg1 = pygame.image.load("C:/PROGRAMMING LANGUAGES/python programming/python snake pr/bg.jpg")
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        bgimg2 = pygame.image.load("C:/PROGRAMMING LANGUAGES/python programming/python snake pr/start.png")
        bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game_Loop()
            gameWindow.blit(bgimg2, (0, 0))
        pygame.display.update()
        clock.tick(60)

def Game_Loop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 450
    snake_y = 300
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    snk_list = []
    snk_length = 1

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(bgimg1, (screen_width, screen_height))
            bgimg3 = pygame.image.load("C:/PROGRAMMING LANGUAGES/python programming/python snake pr/over.jpg")
            bgimg3 = pygame.transform.scale(bgimg3, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg3, (0, 0))
            text_screen("Press Enter To Continue", white, 110, 330)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Game_Loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score += 1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

            gameWindow.fill(white)
            gameWindow.blit(bgimg1, (0, 0))
            text_screen("Score: " + str(score * 10), tomato, 5, 5)
            pygame.draw.rect(gameWindow, cyan, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow, red, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

if __name__ == "__main__":
    welcome()
