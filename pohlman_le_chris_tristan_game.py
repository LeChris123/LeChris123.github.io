import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
offpinky = (112,146,190)
pink = (252, 219, 251)
display_width = 800
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dolphin')
#sets the image used for Fish and snake
icon = pygame.image.load('Fish2.png')
pygame.display.set_icon(icon)

img = pygame.image.load('snakehead2.png')
fishimg = pygame.image.load('Fish2.png')

clock = pygame.time.Clock()
#size of Fish
FishThickness = 30
block_size = 20
FPS = 15

direction = "right"
#sets the font
smallfont = pygame.font.SysFont("papyrus", 25)
medfont = pygame.font.SysFont("papyrus", 50)
largefont = pygame.font.SysFont("papyrus", 80)


def pause():

    paused = True
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")

    message_to_screen("Press C to continue or Q to quit.",
                      black,
                      25)
    pygame.display.update()
#sets the control for the user 
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)
        
        clock.tick(5)
                    

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def randFishGen():
    randFishX = round(random.randrange(0, display_width-FishThickness))/10.0*10.0
    randFishY = round(random.randrange(0, display_height-FishThickness))/10.0*10.0

    return randFishX,randFishY



def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
   #title screen
        gameDisplay.fill(black)
        message_to_screen("Welcome to Dolphin Dash",
                          offpinky,
                          -100,
                          "medium")
        message_to_screen("The objective of the game is to eat fish",
                          white,
                          -30)

        message_to_screen("The more fish you eat, the longer you get",
                          white,
                          10)

        message_to_screen("If you run into yourself, or the edges, you die!",
                          white,
                          50)

        message_to_screen("Press C to play, P to pause or Q to quit.",
                          white,
                          180)
    
        pygame.display.update()
        clock.tick(15)
        
        

#sets control for the block of the snake 
def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, offpinky, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

#generates the location for the fish to spawn
def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randFishX,randFishY = randFishGen()
    
    while not gameExit:

        if gameOver == True:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            #allows restart after fail
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()
            

        while gameOver == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(pink)

        
        #pygame.draw.rect(gameDisplay, red, [randFishX, randFishY, FishThickness, FishThickness])

        gameDisplay.blit(fishimg, (randFishX, randFishY))


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        snake(block_size, snakeList)

        score(snakeLength-1)

        
        pygame.display.update()

        if lead_x > randFishX and lead_x < randFishX + FishThickness or lead_x + block_size > randFishX and lead_x + block_size < randFishX + FishThickness:

            if lead_y > randFishY and lead_y < randFishY + FishThickness:

                randFishX,randFishY = randFishGen()
                snakeLength += 1

            elif lead_y + block_size > randFishY and lead_y + block_size < randFishY + FishThickness:

                randFishX,randFishY = randFishGen()
                snakeLength += 1

            
            

        
            
        
        

        clock.tick(FPS)
        
    pygame.quit()
    quit()

game_intro()
gameLoop()
