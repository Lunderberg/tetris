#!/usr/bin/env python

import pygame
import numpy
import random

board_shape = (10,22)

class Tetris(object):
    def __init__(self):
        self.gamestate = TetrisBoard()
        self.size = 320,240
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            clock.tick(30)
            self.input(pygame.event.get())
            self.timestep()
            self.draw(screen)
            pygame.display.flip()
        pygame.quit()
    def input(self,events):
        for event in events:
            if event.type==pygame.QUIT:
                self.running = False
    def timestep(self):
        pass
    def draw(self,screen):
        screen.fill((0,0,0))
        board_topleft = [0,0]
        width,height = screen.get_size()
        tile_size = min(height/board_shape[1],width/board_shape[0])
        tile = pygame.Surface((tile_size,tile_size))
        tile.fill((255,255,255))
        for i in xrange(board_shape[0]):
            for j in xrange(board_shape[1]):
                val = self.gamestate.board[i,j]
                if val:
                    loc = [board_topleft[0] + tile_size*i,
                           board_topleft[1] + tile_size*(board_shape[1]-j)]
                    screen.blit(tile,loc)



class TetrisBoard(object):
    def __init__(self):
        self.board = numpy.zeros(board_shape,dtype=numpy.int8)
        self.board[5,5] = 1


if __name__=='__main__':
    t = Tetris()
    t.run()
