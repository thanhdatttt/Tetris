#the game class is used for creating the actions of the game 
from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.game_over = False
        self.grid = Grid()
        self.blocks = [IBlock(), Jblock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.cur_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        pygame.mixer.music.load("Tetris/sounds/music.ogg")
        pygame.mixer.music.play(-1)
    
    #update the score
    def updateScore (self, line_clear, move_down_points):
        if line_clear == 1:
            self.score += 100
        elif line_clear == 2:
            self.score += 300
        elif line_clear == 3:
            self.score += 500
        self.score += move_down_points
        
    #create random block
    def get_random_block (self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), Jblock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    #functions to control the block
    def moveLeft (self):
        self.cur_block.move(0, -1)
        if self.blockInside() == False or self.blockFits() == False:
            self.cur_block.move(0, 1)
        
    def moveRight (self):
        self.cur_block.move(0, 1)
        if self.blockInside() == False or self.blockFits() == False:
            self.cur_block.move(0, -1)
        
    def moveDown (self):
        self.cur_block.move(1, 0)
        if self.blockInside() == False or self.blockFits() == False:
            self.cur_block.move(-1, 0)
            self.lockBlock() 
    
    def rotate (self):
        self.cur_block.rotate()
        if self.blockInside() == False or self.blockFits() == False:
            self.cur_block.undoRotate()
    
    #check the block is in the grid or not
    def blockInside (self):
        tiles = self.cur_block.get_cell_positions()
        for tile in tiles:
            if self.grid.isInside(tile.row, tile.column) == False:
                return False
        return True
    
    #lock the block if it reaches the end of the grid and get the new block
    def lockBlock (self):
        tiles = self.cur_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.cur_block.id
        self.score += 1
        self.cur_block = self.next_block
        self.next_block = self.get_random_block()
        row_clear = self.grid.clearFullRow()
        
        #updating the score
        self.updateScore(row_clear, 0)
        
        #check for the game over
        if self.blockFits() == False:
            self.game_over = True
        
    def blockFits (self):
        tiles = self.cur_block.get_cell_positions()
        for tile in tiles:
            if self.grid.isEmpty(tile.row, tile.column) == False:
                return False
        return True
    
    #reset to a new game
    def reset (self):
        self.grid.reset()
        self.blocks = [IBlock(), Jblock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.cur_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        
    #draw the block on the screen
    def draw (self, win):
        self.grid.draw(win)
        self.cur_block.draw(win, 1, 1)
        
        if self.next_block.id == 3:
            self.next_block.draw(win, 305, 250)
        elif self.next_block.id == 4:
            self.next_block.draw(win, 340, 250)
        elif self.next_block.id == 5:
            self.next_block.draw(win, 450, 250)
        else:
            self.next_block.draw(win, 320, 270)