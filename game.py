## REQUIRED MODULES ##
# Importere biblioteker #
import random
import time
import pygame as pg

from pacman import PacMan
from ghost import Ghost
from level import Level


## SETUP ##
# Opstiller spillets "level" og scaler x,y koordinater til spilskærmen#
pg.init()
level = Level("level.txt")

width = level.num_cols * 32
height = level.num_cols * 32
screen = pg.display.set_mode((width, height))

# Opstiller startskærm og vinduets navn #
pg.display.set_caption("Fucked up Pac-Man")
font = pg.font.Font(None, 32)


## GAME LOOP ##
# Klargøre variabler til gameloop #
direction = None
tick = 0
state = "LOAD"
points = 0
running = True

# WhileLoop/GameLoop #
while running:
    
    # Initiere classes til variabler #
    if state == "LOAD":
        pacman = PacMan(level.pacman_x, level.pacman_y)
        ghost = Ghost(level.ghost_x, level.ghost_y)
        direction = None
        state = "READY"

    # Loader startskærmen (Font, størrelse og tekst) #
    elif state == "READY":
        text = font.render("Press [Enter] to play", True, (220,220,10))
        text_rect = text.get_rect(center=(8*32/2, 7*32/2)) 
        screen.blit(text, text_rect)

        # Definerer "enter" og "exit" for at starte og slutte spillet # 
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    state = "PLAY"  

        # Opdatere display og hele programmet delayer i 0.1 sekundt #
        pg.display.flip()  
        time.sleep(0.1)
        
    # Hvis man er igang med spillet "play", så sker understående: #
    elif state == "PLAY": 

        ## HANDLE EVENTS (keypresses etc.) ##
        events = pg.event.get()
        for event in events:

            # Lukker vinduet, mens man spiller (e.g. pressing [x] or Ctrl+F4) #
            if event.type == pg.QUIT:
                running = False
            
            # Keyboard defineringer, controls (som vi bruger i pacman.py) #
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    direction = "up"
                elif event.key == pg.K_DOWN:
                    direction = "down"
                elif event.key == pg.K_LEFT:
                    direction = "left"
                elif event.key == pg.K_RIGHT:
                    direction = "right"
                elif event.key == pg.K_ESCAPE:
                    running = False


        ## MOVE / LOGIC ##
        # Kalder variablernes movefunktion #
        # level og direction gør det muligt at 
        # anvende i pacman og ghost funktioner #
        pacman.move(level, direction)
        ghost.move(level)

        # Hvis pacman er i x,y koordinatet for "." #
        # vil point += 1, og ryder feltet " " #
        if level.tiles[pacman.row][pacman.col] == ".":
            points += 1
            level.tiles[pacman.row][pacman.col] = " "

        ## Draw ##
        # Fylder skærmen til sort, variablerne tegner classerne #
        screen.fill((0,0,0))
        level.draw(screen)
        ghost.draw(screen)
        pacman.draw(screen,direction)

        ## POINT RENDER ##
        # Render font og skriver tekst #
        # Insætter tekst i rectangle, med spawnpoint i venstre hjørne #
        # Indsætter tekst på skærmen #
        pointsText = font.render(f"Points: {points}", True, (220, 220, 10))
        pointsText_rect = pointsText.get_rect(bottomleft = (0 , height))
        screen.blit(pointsText, pointsText_rect)

        # Update window with newly drawn pixels
        pg.display.flip()  

        # Limit framerate by waiting a 10-100 milliseconds
        time.sleep(0.15)