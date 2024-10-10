import pygame, sys
#import the classes
from grid import Grid
from game import Game
from colors import Colors

#game initialization
pygame.init()

#create interface (score, next block and the game over)
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("SCORE", True, Colors.white)
next_surface = title_font.render("NEXT", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)


score_rect = pygame.Rect(420, 55, 170, 60)
next_rect = pygame.Rect(420, 215, 170, 180)

#create game screen
win = pygame.display.set_mode((600, 820))
pygame.display.set_caption("Tetris game")

#set fps
clock = pygame.time.Clock()

#create blocks
game = Game()

#create the timer for spawning block
game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 500)

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #control button 
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.moveLeft()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.moveRight()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.moveDown()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == game_update and game.game_over == False:
            game.moveDown()
            
    #display score on the screen
    score_val_surface = title_font.render(str(game.score), True, Colors.white)
    
    #draw the screen
    win.fill(Colors.dark_blue)
    win.blit(score_surface, (455, 20, 20, 50))
    win.blit(next_surface, (465, 180, 50, 50))
    if game.game_over == True:
        win.blit(game_over_surface, (420, 550, 50, 50))
    
    pygame.draw.rect(win, Colors.light_blue, score_rect, 0, 10)
    win.blit(score_val_surface, score_val_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(win, Colors.light_blue, next_rect, 0, 10)
    game.draw(win)

    pygame.display.update()
    
    clock.tick(120)