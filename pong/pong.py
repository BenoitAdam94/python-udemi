import pygame

# game settings

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

COLOR_BLACK = 0, 0, 0
COLOR_GREEN = 166, 206, 57

TEXT_PADDING = 25
PADDLE_SPEED = 5
PADDLE_OFFSET = 10
BALL_SPEED = 3
SPIN_PERCENT = 0.5

# functions

def update(elapsedTime):
    return None

def draw():
    return None
    
# initialisation
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# loop control and timing
gameover = False

lastTick = pygame.time.get_ticks()
elapsedTime = 0

# gameloop
while not gameover:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN and event.type == pygame.K_ESC:
            gameover = True
    
    elapsedTime = pygame.time.get_ticks() - lastTick
    lastTick = pygame.time.get_ticks()
    
    update(elapsedTime)
    draw
        
