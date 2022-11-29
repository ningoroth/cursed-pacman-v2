import pygame as pg

class Level:

    def __init__(self, file):

        self.tiles = []
        with open(file, "r") as level_file:
            for line in level_file:
                line = line.rstrip("\r\n") # Remove line endings
                row = []
                for character in line:
                    if character == "#":
                        row.append("#")
                    else: 
                        row.append(".")
                    #elif char == "p":
                        #y = r*32
                        #x = c*32
                        #row.append(" ")
                self.tiles.append(row)
        
        num_rows = len(self.tiles)
        num_cols = len(self.tiles[0])


    def draw(self, screen):
        for row_idx, row in enumerate(self.tiles):
            for col_idx, tile in enumerate(row):
                if tile == "#":
                    pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 1)
