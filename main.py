import pygame
import random
import os
import sys

def resource_path(filename):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gloobls!")

BackgroundFrame1 = pygame.image.load(resource_path("BackgroundFrame1.png")).convert_alpha()
BackgroundFrame1 = pygame.transform.scale(BackgroundFrame1, (800, 600))
BackgroundFrame2 = pygame.image.load(resource_path("BackgroundFrame2.png")).convert_alpha()
BackgroundFrame2 = pygame.transform.scale(BackgroundFrame2, (800, 600))
BackgroundFrame3 = pygame.image.load(resource_path("BackgroundFrame3.png")).convert_alpha()
BackgroundFrame3 = pygame.transform.scale(BackgroundFrame3, (800, 600))
BackgroundFrames = [BackgroundFrame1, BackgroundFrame2, BackgroundFrame3]

GameOverScreen = pygame.image.load(resource_path("Gameover.png")).convert_alpha()
GameOverScreen = pygame.transform.scale(GameOverScreen, (window.get_width(), window.get_height()))

Floor = pygame.surface.Surface((800, 300))
Floor.fill((148, 93, 138))
Ground = pygame.surface.Surface((800, 300))
Ground.fill((92, 69, 88))

playergloobl = pygame.image.load(resource_path("Playergloobl.png")).convert_alpha()
playergloobl = pygame.transform.scale(playergloobl, (50, 50))
playerglooblrotation = 0

Gloobl1 = pygame.image.load(resource_path("Gloob1.png")).convert_alpha()
Gloobl1 = pygame.transform.scale(Gloobl1, (100, 100))
Gloobl2 = pygame.image.load(resource_path("Gloob2.png")).convert_alpha()
Gloobl2 = pygame.transform.scale(Gloobl2, (100, 100))
Gloobl3 = pygame.image.load(resource_path("Gloob3.png")).convert_alpha()
Gloobl3 = pygame.transform.scale(Gloobl3, (100, 100))
Gloobl4 = pygame.image.load(resource_path("Gloob4.png")).convert_alpha()
Gloobl4 = pygame.transform.scale(Gloobl4, (100, 100))

Gloobl1_x = 50
Gloobl1_y = 0
Gloobl1_vel_x = 0
Gloobl1_vel_y = 0
Gloobl2_x = 200
Gloobl2_y = 0
Gloobl2_vel_x = 0
Gloobl2_vel_y = 0
Gloobl3_x = 430
Gloobl3_y = 0
Gloobl3_vel_x = 0
Gloobl3_vel_y = 0
Gloobl4_x = 500
Gloobl4_y = 0
Gloobl4_vel_x = 0
Gloobl4_vel_y = 0

player_x = 350
player_y = 350
player_vel_x = 0
player_vel_y = 0

def playerhitbox(playergloobl_x, player_gloobl_y):
    return pygame.Rect(playergloobl_x, player_gloobl_y, 50, 50)

def gloobl1hitbox(gloobl1_x, gloobl1_y):
    return pygame.Rect(gloobl1_x, gloobl1_y, 75, 75)

def gloobl2hitbox(gloobl2_x, gloobl2_y):
    return pygame.Rect(gloobl2_x, gloobl2_y, 90, 90)

def gloobl3hitbox(gloobl3_x, gloobl3_y):
    return pygame.Rect(gloobl3_x, gloobl3_y, 100, 100)

def gloobl4hitbox(gloobl4_x, gloobl4_y):
    return pygame.Rect(gloobl4_x, gloobl4_y, 90, 90)

def Gloobl1Collisiondetection(playerhitbox, gloobl1hitbox):
    return playerhitbox.colliderect(gloobl1hitbox)

def Gloobl2Collisiondetection(playerhitbox, gloobl2hitbox):
    return playerhitbox.colliderect(gloobl2hitbox)

def Gloobl3Collisiondetection(playerhitbox, gloobl3hitbox):
    return playerhitbox.colliderect(gloobl3hitbox)

def Gloobl4Collisiondetection(playerhitbox, gloobl4hitbox):
    return playerhitbox.colliderect(gloobl4hitbox)

StartTime = pygame.time.get_ticks()
CurrentTime = 0

Gloobl1Rotate = 0
Gloobl2Rotate = 0
Gloobl3Rotate = 0
Gloobl4Rotate = 0
Gloobl1RotationDirection = random.uniform(-1, 1)
Gloobl2RotationDirection = random.uniform(-1, 1)
Gloobl3RotationDirection = random.uniform(-1, 1)
Gloobl4RotationDirection = random.uniform(-1, 1)

GameFont = pygame.font.Font(resource_path("augiepixel.ttf"), 75)
TitleFont = pygame.font.Font(resource_path("augiepixel.ttf"), 130)

TitleText = TitleFont.render("GLOOBLS!", True, (0, 255, 255))
PlayText = TitleFont.render("PLAY!?!?", True, (255, 255, 255))
PlayTextRect = PlayText.get_rect(topleft=(100, 300))

Game_state = "Title"
while True:
    BackgroundTime = pygame.time.get_ticks()
    CurrentTime = pygame.time.get_ticks()
    GameTimer = (CurrentTime - StartTime) // 1000
    TimerText = GameFont.render(str(f"Time: {GameTimer}"), True, (158, 232, 255))
    if CurrentTime - BackgroundTime >= 500:
        BackgroundFrames.append(BackgroundFrames.pop(0))
        StartTime = CurrentTime
    for event in pygame.event.get():
        MousePosition = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            quit(0)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -2

            if event.key == pygame.K_RIGHT:
                player_vel_x = 2
        else:
            player_vel_x = 0
            player_vel_y = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePosition == pygame.mouse.get_pos()
            if PlayTextRect.collidepoint(MousePosition):
                Game_state = "Playing"

    if Gloobl1_y >= window.get_height():
        Gloobl1_y = 0
        Gloobl1_x = random.randint(0, window.get_height() - 100)

    if Gloobl2_y >= window.get_height():
        Gloobl2_y = 0
        Gloobl2_x = random.randint(0, window.get_height() - 100)

    if Gloobl3_y >= window.get_height():
        Gloobl3_y = 0
        Gloobl3_x = random.randint(0, window.get_height() - 100)

    if Gloobl4_y >= window.get_height():
        Gloobl4_y = 0
        Gloobl4_x = random.randint(0, window.get_height() - 100)
        
    if Game_state == False:
        window.blit(GameOverScreen, (0, 0))
        Gloobl1_vel_y = 0
        Gloobl2_vel_y = 0
        Gloobl3_vel_y = 0
        Gloobl4_vel_y = 0
    
    PlayerHitbox = playerhitbox(player_x, player_y)
    Gloobl1Hitbox = gloobl1hitbox(Gloobl1_x, Gloobl1_y)
    Gloobl2Hitbox = gloobl2hitbox(Gloobl2_x, Gloobl2_y)
    Gloobl3Hitbox = gloobl3hitbox(Gloobl3_x, Gloobl3_y)
    Gloobl4Hitbox = gloobl4hitbox(Gloobl4_x, Gloobl4_y)

    if Gloobl1Collisiondetection(PlayerHitbox, Gloobl1Hitbox):
        Game_state = "Dead"

    if Gloobl2Collisiondetection(PlayerHitbox, Gloobl2Hitbox):
        Game_state = "Dead"
        
    if Gloobl3Collisiondetection(PlayerHitbox, Gloobl3Hitbox):
        Game_state = "Dead"

    if Gloobl4Collisiondetection(PlayerHitbox, Gloobl4Hitbox):
        Game_state = "Dead"
    Gloobl1_x += Gloobl1_vel_x
    Gloobl1_y += Gloobl1_vel_y
    Gloobl1Rotate += Gloobl1RotationDirection

    Gloobl2_x += Gloobl2_vel_x  
    Gloobl2_y += Gloobl2_vel_y
    Gloobl2Rotate += Gloobl2RotationDirection

    Gloobl3_x += Gloobl3_vel_x
    Gloobl3_y += Gloobl3_vel_y
    Gloobl3Rotate += Gloobl3RotationDirection

    Gloobl4_x += Gloobl4_vel_x
    Gloobl4_y += Gloobl4_vel_y
    Gloobl4Rotate += Gloobl4RotationDirection

    player_x += player_vel_x
    player_y += player_vel_y

    if Game_state == "Title":
        window.blit(TitleText, (80, 100))
        window.blit(PlayText, (100, 300))

    elif Game_state == "Playing":
        window.blit(BackgroundFrames[0], (0, 0))
        window.blit(TimerText, (100, 10))
        playerglooblrotation += 1
        RotatedPlayer = pygame.transform.rotate(playergloobl, playerglooblrotation)
        window.blit(RotatedPlayer, (player_x, player_y))
        window.blit(Floor, (0, 400))
        window.blit(Ground, (0, 430))
        Gloobl1_vel_y = 2
        Gloobl2_vel_y = 2
        Gloobl3_vel_y = 2
        Gloobl4_vel_y = 2
        RotatedGloobl1 = pygame.transform.rotate(Gloobl1, Gloobl1Rotate)
        RotatedGloobl2 = pygame.transform.rotate(Gloobl2, Gloobl2Rotate)
        RotatedGloobl3 = pygame.transform.rotate(Gloobl3, Gloobl3Rotate)
        RotatedGloobl4 = pygame.transform.rotate(Gloobl4, Gloobl4Rotate)
        window.blit(RotatedGloobl1, (Gloobl1_x, Gloobl1_y))
        window.blit(RotatedGloobl2, (Gloobl2_x, Gloobl2_y))
        window.blit(RotatedGloobl3, (Gloobl3_x, Gloobl3_y))
        window.blit(RotatedGloobl4, (Gloobl4_x, Gloobl4_y))
    elif Game_state == "Dead":
        window.blit(GameOverScreen, (0, 0))
    pygame.display.flip()
    clock.tick(60)