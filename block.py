import pygame
from colors import Colors
from position import Position

class Block:
    #initialization
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 40
        self.row_offset = 0 #the rows that the cell has moved
        self.col_offset = 0 #the cols that the cell has moved
        self.rotation_state = 0 #the state of the cell when it rotate
        self.color = Colors.get_cell_colors()
    
    #move the block
    def move (self, rows, columns):
        self.row_offset += rows
        self.col_offset += columns
    
    #get the new positions of the block  
    def get_cell_positions (self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.col_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    #rotate the block
    def rotate (self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0
    
    def undoRotate (self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1
            
    #draw blocks
    def draw(self, win, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            #rect(x, y, width, height)  
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, offset_y + tile.row * self.cell_size , self.cell_size -1, self.cell_size -1)
        
            pygame.draw.rect(win, self.color[self.id], tile_rect)