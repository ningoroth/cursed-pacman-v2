## REQUIRED MODULES ##
# Importerer biblioteker #
import pygame as pg

# Starter klassen "Level" #
class Level:

    # Definerer funktionen __init__ (Kaldes via "Level(args)") #
    def __init__(self, file):

        # Definerer en liste til alle level-tiles #
        self.tiles = []

        # Åbner filen "level.txt" i læsefunktion (read / "r") #
        with open(file, "r") as level_file:
            for r, line in enumerate(level_file):
                # Definerer listen med rækker i level #
                row = []

                # Bruger "line" fra "level.txt" til at finde forskellige karakterer herunder; "#", ".", "p", "g" #
                for c, char in enumerate(line):
                    # "#" er væggene i level #
                    if char == "#":
                        row.append("#")

                    # "." er points i level #
                    elif char == ".":
                        row.append(".")

                    # "p" er pacman i level #
                    elif char == "p":
                        self.pacman_x = r
                        self.pacman_y = c
                        row.append(" ")

                    # "g" er spøgelset i level #
                    elif char == "g":
                        self.ghost_x = r
                        self.ghost_y = c
                        row.append(" ")

                    # Alt andet (mellemrum) er " " #
                    else:
                        row.append(" ")
                
                # Tilføjer listen med alle rækker til listen med alle level-tiles #
                self.tiles.append(row)
        
        # Definerer længden og højden af hele levelet ved at finde længden af "self.tiles" horisontalt og vertikalt #
        self.num_rows = len(self.tiles)
        self.num_cols = len(self.tiles[0]) 

    # Definerer funktionen til at tegne level #
    def draw(self, screen):

        # Looper hver enkel tile i "self.tiles" og leder efter alle vægge ("#") og points (".") #
        for row_idx, row in enumerate(self.tiles):
            for col_idx, tile in enumerate(row):
                if tile == "#":
                    # Tegner en blå firkant ved alle "#" #
                    pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 100)
                elif tile == ".":
                    # Tegner en hvid cirkel ved alle "." #
                    pg.draw.circle(screen, (255,255,255), (col_idx*32+1+16, row_idx*32+1+16), 5)
        