import pygame as pg

class Level:

    def __init__(self, file):

        self.tiles = []
        with open(file, "r") as level_file:
            for r, line in enumerate(level_file):
                rows = []
                for c, char in enumerate(line):
                    if char == "#":
                        rows.append("#")
                    elif char == "p":
                        self.x = r * 32
                        self.y = c * 32
                        rows.append(" ")
                    else:
                        rows.append(" ")
                
                self.tiles.append(rows)
        
        num_rows = len(level)
        num_cols = len(level[0])
                    

            #for line in level_file:
            #    line = line.rstrip("\r\n") # Remove line endings
            #    row = []
            #    for character in line:
            #        row.append(character)
            #    self.tiles.append(row)
            


    def draw(self, screen):
        for row_idx, row in enumerate(self.tiles):
            for col_idx, tile in enumerate(row):
                if tile == "#":
                    pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 1)


        