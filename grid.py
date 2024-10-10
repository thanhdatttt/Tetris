#grid class is uesed to create a matrix on the screen for the game
import pygame
from colors import Colors

class Grid:
    #initialization
    def __init__(self):
        self.nrow = 20
        self.ncol = 10
        self.cell_size = 40
        self.grid = [[0 for j in range(self.ncol)] for i in range(self.nrow)]
        self.colors = Colors.get_cell_colors()
        
    def printGrid (self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                print(self.grid[i][j], end= ' ')
            print()  
    
    #check if the block is in the grid or not
    def isInside (self, row, column):
        if row >= 0 and row < self.nrow and column >= 0 and column < self.ncol:
            return True
        return False
    
    #check if the place has a block or not
    def isEmpty (self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    #check for a completed row, if it is, clear the row and move all the row down
    def isCompletedRow (self, row):
        for col in range(self.ncol):
            if self.grid[row][col] == 0:
                return False
        return True
    
    def clearRow (self, row):
        for col in range(self.ncol):
            self.grid[row][col] = 0
    
    def moveRowDown (self, row, nrow):
        for col in range(self.ncol):
            self.grid[row + nrow][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    def clearFullRow (self):
        completed = 0
        for row in range(self.nrow -1, 0, -1):
            if self.isCompletedRow(row):
                self.clearRow(row)
                completed += 1
            elif completed > 0:
                self.moveRowDown(row, completed)
        return completed
    
    #reset the grid for a new game
    def reset (self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                self.grid[i][j] = 0
                  
    #draw the grid on the game screen
    def draw(self, win):
        for i in range(self.nrow):
            for j in range(self.ncol):
                cell_val = self.grid[i][j]
                #cell rectangle (x, y, width, height)
                cell_rect = pygame.Rect(j * self.cell_size + 1, i * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
                
                pygame.draw.rect(win, self.colors[cell_val], cell_rect)
                