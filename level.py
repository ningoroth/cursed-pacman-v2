import pygame as pg

class Level:

    def __init__(self, file):

        self.tiles = []
        with open(file, "r") as level_file:
            for r, line in enumerate(level_file):
                row = []
                for c, char in enumerate(line):
                    if char == "#":
                        row.append("#")

                    elif char == ".":
                        row.append(".")

                    elif char == "p":
                        self.pacman_x = r
                        self.pacman_y = c
                        row.append(" ")

                    elif char == "g":
                        self.ghost_x = r
                        self.ghost_y = c
                        row.append(" ")

                    else:
                        row.append(" ")
                
                self.tiles.append(row)
        
        self.num_rows = len(self.tiles)
        self.num_cols = len(self.tiles[0]) 

    def draw(self, screen):
        for row_idx, row in enumerate(self.tiles):
            for col_idx, tile in enumerate(row):
                if tile == "#":
                    pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 100)
                elif tile == ".":
                    pg.draw.circle(screen, (255,255,255), (col_idx*32+1+16, row_idx*32+1+16), 5)


        