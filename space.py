import pygame
from pygame.key import *
from pygame import mixer
import random

pygame.init()

screen = pygame.display.set_mode([800, 600]) #sets the width and height of the initial screen
pygame.display.set_caption("Python game!") #sets the name of the display screen
icon = pygame.image.load("sock.jpg").convert_alpha() #to set icon image
pygame.display.set_icon(icon)

background = pygame.image.load("space.jpg").convert_alpha() #preface for bg

#background sound
mixer.music.load("hacker.wav")
mixer.music.play(-1)

score = 0 #set score as 0

#Player
player_image = pygame.image.load("spaceship.png").convert_alpha()
playerx = 370
playery = 480
playerx_change = 0
playery_change = 0

def player(x, y):
    screen.blit(player_image, (x, y)) #draws the image onto the surface

#enemy
enemy_image = pygame.image.load("alien.png").convert_alpha()
enemy_image2 = pygame.image.load("alien2.png").convert_alpha()
enemyx = random.randint(0, 736)
enemyy = random.randint(80, 536) 
enemyx_change = 0.5
enemyy_change = 0.5

def enemy(x, y):
    if score % 2 == 0:
        screen.blit(enemy_image, (x, y))
    else:
        screen.blit(enemy_image2, (x, y))
    

#bullet
bullet_image = pygame.image.load("bullet.png").convert_alpha()
bulletx = playerx 
bullety = playery
bulletx_change = 0
bullety_change = 0
bullet_state = "ready"

def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 12, y + 6)) #fix it so its in the middle

#score
score = 0
def score_font(x, y): 
    global score
    font = pygame.font.Font("freesansbold.ttf", 30)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

#game over
def game_over():
        over_font = pygame.font.Font("freesansbold.ttf", 64)
        end = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(end, (200, 250))


running = True
while running:
    screen.fill((0, 0, 0)) #fills screen w black

    screen.blit(background, (0, 0)) #puts bg on top of black screen

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound("laser.wav")
                bullet_sound.play()
                bulletx = playerx
                bullety = playery
                bullet(bulletx, bullety)
            if event.key == pygame.K_UP:
                playery_change = -0.6
            if event.key == pygame.K_DOWN:
                playery_change = 0.6
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.6
            if event.key == pygame.K_LEFT:
                playerx_change = -0.6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playery_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    playerx_change = 0
        elif event.type == pygame.QUIT:
            running = False

    if bullet_state == "fire":
        bullety_change = -0.5
        bullety += bullety_change
        bullet(bulletx, bullety)
    
    #bulletx = playerx
    #bullety = playery

    if bullet_state == "fire" and bullety != playery:
        if enemyx < bulletx + 16 < enemyx + 64:
            if enemyy < bullety < enemyy + 58 or enemyy < bullety + 60 < enemyy + 58:
                enemy_boom = mixer.Sound("explosion.wav")
                enemy_boom.play()
                enemyx = random.randint(0, 736)
                enemyy = random.randint(80, 536)
                score += 1
                bullet_state == "ready"

    if enemyx < playerx < enemyx + 64 or enemyx < playerx + 64 < enemyx + 64:
       if enemyy < playery < enemyy + 54 or enemyy < playery + 58 < enemyy + 54:   
            game_over()
            break

    playerx += playerx_change
    playery += playery_change

    if playerx <= 0: 
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    elif playery <= 0:
        playery = 0 
    elif playery >= 542:
        playery = 542

    enemyx += enemyx_change
    enemyy += enemyy_change

    if enemyx <= 0:
        enemyx_change = 0.5
    elif enemyx >= 736:
        enemyx_change = -0.5
    elif enemyy <= 0:
        enemyy_change = 0.5
    elif enemyy >= 546:
        enemyy_change = -0.5

    player(playerx, playery) #puts player in the loop so it stays on the screen while game runs
    enemy(enemyx, enemyy) #puts enemy in loop
    score_font(10, 10) #puts it in loop

    pygame.display.update()
    

    
