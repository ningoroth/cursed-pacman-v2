## REQUIRED MODULES ##
# Importerer biblioteker #
import pygame as pg
import random
from pacman import PacMan

## GHOST CLASS ##
class Ghost:

    # Definerer ghost parameteren (self) x,y koordinater #
    def __init__(self, row, col):

        ## MOVE SOUND ##
        # Indsætter lyd mens move funktionen er aktiv #
        # https://sfxr.me/#34T6PktF8TcRjBGBCtaWAp8xrJeEmwSfouC2KVwAWC42iM2UWcDqruxhd8Xq4MFBc7kMaDGuyeyqde9ddiWDHprGh2dvs6Ery9NZQmbQM9gyXmSZzdhxPnMnw
        # https://sfxr.me/#34T6PkpqAUU8XZ3ze41FCou6ZCuAPdnvQEjkm2P1TPRMxjSRZdiQm9e5DJF1dPTvN8C3gPXJ7DuFniwZVHsmDC5qDkCUYDnkkgQAsqe9MaC2pHxKexVqdd5Jw
        self.sound_move0 = pg.mixer.Sound("sounds/pacman_move_0.wav")
        self.sound_move1 = pg.mixer.Sound("sounds/pacman_move_1.wav")
        self.sound_move0.set_volume(0.5)
        self.sound_move1.set_volume(0.5)

        # Sætter parameter variablen til en ny parameter #
        self.col = col
        self.row = row

        ## LOAD IMAGES ##
        # Loader billeder fra mappen ghostsImages, scalerer størrelse #
        # Intergerer img til listen #
        self.images = []
        for i in range(2):
            img = pg.image.load(f"images/ghostsImages/pink_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

        self.tick = 0
   
    # Definerer metoden find pacman, så classen kan finde pacman #
    def find_pacman(self):
        self.col = -1
        self.row = -1
        print(self.col, self.row)

    # Definerer metoden move, hvor classen bevæger sig randomt mellem -1 +1 #
    def move(self, level):
        self.col += random.randint(-1,1)
        self.row += random.randint(-1,1)
        
        # Så ghost ikke kan bevæge sig ud af map og vil bevæges tilbage ind #
        if self.col < 0:
            self.col += 1

        elif self.col == level.num_cols:
            self.col -= 1

        elif self.row < 0:
            self.row += 1
    
        elif self.row == level.num_rows:
            self.row -= 1

        self.tick += 1 
    
    # Definerer draw, og tegner billed %2, sætter spawn. #
    def draw(self,screen):
        r = self.tick%2
        screen.blit(self.images[r], (self.col*32, self.row*32)) 