import pygame as pg
import random

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
            img = pg.image.load(f"images/ghostsImages/pink_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

        self.tick = 0


    def move(self, level):
        self.col += random.randint(-1,1)
        self.row += random.randint(-1,1)

        self.tick += 1 
    
    def draw(self, tick, screen, pinkGhost):
        self.ghostDirection = random.choice(["left", "right", "up", "down"])
        print("draw:", self.ghostDirection)
        r = int((tick/2)%4)
        if self.ghostDirection == "right":
            screen.blit(pinkGhost[0], (self.x, self.y))
        elif self.ghostDirection == "up":
            screen.blit(pinkGhost[1], (self.x, self.y))
        elif self.ghostDirection == "left":
            screen.blit(pinkGhost[2], (self.x, self.y))
        elif self.ghostDirection == "down":
            screen.blit(pinkGhost[3], (self.x, self.y))
        else:
            screen.blit(pinkGhost[0], (self.x, self.y))
    
    def draw(self,screen):
        r = self.tick%2
        screen.blit(self.images[r], (self.col*32, self.row*32)) 