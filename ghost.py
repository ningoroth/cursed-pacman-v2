import pygame as pg
import random
from pacman import PacMan

class Ghost:

    def __init__(self, row, col):

        # https://sfxr.me/#34T6PktF8TcRjBGBCtaWAp8xrJeEmwSfouC2KVwAWC42iM2UWcDqruxhd8Xq4MFBc7kMaDGuyeyqde9ddiWDHprGh2dvs6Ery9NZQmbQM9gyXmSZzdhxPnMnw
        # https://sfxr.me/#34T6PkpqAUU8XZ3ze41FCou6ZCuAPdnvQEjkm2P1TPRMxjSRZdiQm9e5DJF1dPTvN8C3gPXJ7DuFniwZVHsmDC5qDkCUYDnkkgQAsqe9MaC2pHxKexVqdd5Jw
        self.sound_move0 = pg.mixer.Sound("sounds/pacman_move_0.wav")
        self.sound_move1 = pg.mixer.Sound("sounds/pacman_move_1.wav")
        self.sound_move0.set_volume(0.5)
        self.sound_move1.set_volume(0.5)

        self.col = col
        self.row = row

        self.images = []
        for i in range(2):
            img = pg.image.load(f"images/ghost_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

        self.tick = 0
   
    def find_pacman(self):
        self.col = -1
        self.row = -1
        print(self.col, self.row)

        for x in range(len(self)):
            for row in range(len(self[x])):
                if self[self.col,self.row] == "P":
                    self.col = self.col
                    self.row = row
        return self.col, self.row

    def move(self):
        dx = random.randint(-2,2)
        dy = random.randint(-2,2)
        self.col += dx
        self.row += dy
    
    def draw(self,screen):
        r = self.tick%2
        screen.blit(self.images[r], (self.col*32, self.row*32)) 