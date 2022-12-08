## REQUIRED MODULES ##
# Importerer biblioteker #
import pygame as pg

## PACMAN CLASS ##
class PacMan:

    # Definerer pacman parameteren (self) x,y koordinater #
    def __init__(self, row, col):

        ## MOVE SOUND ##
        # Indsætter lyd mens move funktionen er aktiv #
        # https://sfxr.me/#34T6PktF8TcRjBGBCtaWAp8xrJeEmwSfouC2KVwAWC42iM2UWcDqruxhd8Xq4MFBc7kMaDGuyeyqde9ddiWDHprGh2dvs6Ery9NZQmbQM9gyXmSZzdhxPnMnw
        # https://sfxr.me/#34T6PkpqAUU8XZ3ze41FCou6ZCuAPdnvQEjkm2P1TPRMxjSRZdiQm9e5DJF1dPTvN8C3gPXJ7DuFniwZVHsmDC5qDkCUYDnkkgQAsqe9MaC2pHxKexVqdd5Jw
        self.sound_move0 = pg.mixer.Sound("sounds/pacman_move_0.wav")
        self.sound_move1 = pg.mixer.Sound("sounds/pacman_move_1.wav")
        self.sound_move0.set_volume(0.01) #0.5
        self.sound_move1.set_volume(0.01) #0.5

        # Sætter parameter variablen til en ny parameter #
        self.col = col
        self.row = row

        ## LOAD IMAGES ##
        # Loader billeder fra mappen pacmanImages, scalerer størrelse #
        # Intergerer img til listen #
        self.images = []
        for i in range(6):
            img = pg.image.load(f"images/pacmanImages/pacman_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

        self.tick = 0


    # Definerer metoden move #
    def move(self, level, direction):

        # Laver hitbox til pacman, hvis directionen "#": #
        moving = False
        if direction == "up":
            if level.tiles[self.row-1][self.col] != "#":
                self.row -= 1
                moving = True

        elif direction == "down":
            if level.tiles[self.row+1][self.col] != "#":
                self.row += 1
                moving = True

        elif direction == "left":
            if level.tiles[self.row][self.col-1] != "#":
                self.col -= 1
                moving = True

        elif direction == "right":
            if level.tiles[self.row][self.col+1] != "#":
                self.col += 1 
                moving = True

        if self.col < 0:
            self.col = level.num_cols -1
        
        elif self.col == level.num_cols:
            self.col = 0

        if moving:
            if self.tick%2 == 0:
                self.sound_move0.play()
            else:
                self.sound_move1.play()

        self.tick += 1 
    
    # Definerer draw, og tegner billederne når pacman vender, sætter spawn. #
    def draw(self, screen, direction):
        r = int((self.tick/1)%6)
        if direction == "left":
            screen.blit(self.images[r], (self.col*32, self.row*32))
        elif direction == "right":
            screen.blit(pg.transform.rotate(self.images[r],180), (self.col*32, self.row*32))
        elif direction == "up":
            screen.blit(pg.transform.rotate(self.images[r],-90), (self.col*32, self.row*32))
        elif direction == "down":
            screen.blit(pg.transform.rotate(self.images[r],90), (self.col*32, self.row*32))
        else:
            screen.blit(self.images[0], (self.col*32, self.row*32))