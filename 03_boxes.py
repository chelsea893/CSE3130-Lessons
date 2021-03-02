'''
title: boxes
author: Chelsea Chen
date-created: 2021-03-02
'''

import pygame
from myClasses import Window, Color

class Box:
    """
    Creates a box
    """

    def __init__(self, WIDTH = 1, HEIGHT = 1, X = 0, Y= 0, COLOR= Color.WHITE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.X = X
        self.Y = Y
        self.POS = (self.X, self.Y)
        self.SCREEN = pygame.Surface(self.DIMENSION, pygame.SRCALPHA, 32)
        self.COLOR = COLOR
        self.SCREEN.fill(self.COLOR)
        self.SPD = 5


    # --- MODIFIER METHODS --- #

    def moveBox(self, KEYPRESSES):
        # CHECK KEYPRESSES
        if KEYPRESSES[pygame.K_d] == 1:
            self.X = self.X + self.SPD
        if KEYPRESSES[pygame.K_a] == 1:
            self.X -= self.SPD
        if KEYPRESSES[pygame.K_w] == 1:
            self.Y -= self.SPD
        if KEYPRESSES[pygame.K_s] == 1:
            self.Y += self.SPD

        self.POS = (self.X, self.Y)

        # CHECK BOUNDARIES
    def checkBoundaries(self,MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH = 0, MIN_HEIGHT = 0):
        if self.X > MAX_WIDTH -self.SCREEN.get_rect().width:
            self.X = MAX_WIDTH -self.SCREEN.get_rect().width
        elif self.X < MIN_WIDTH:
            self.X = MIN_WIDTH
        if self.Y > MAX_HEIGHT -self.SCREEN.get_rect().height:
            self.Y = MAX_HEIGHT - self.SCREEN.get_rect().height
        elif self.Y< MIN_HEIGHT:
            self.Y = MIN_HEIGHT

        self.POS = (self.X, self.Y)

    def moveBoxChkBoundaries(self, KEYPRESSES, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        self.moveBox(KEYPRESSES)
        self.checkBoundaries(MAX_WIDTH,MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT)

    def wrapBox(self,MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH = 0, MIN_HEIGHT = 0):
        if self.X > MAX_WIDTH:
            self.X = -self.SCREEN.get_rect().width
        elif self.X < MIN_WIDTH - self.SCREEN.get_rect().width:
            self.X = MAX_WIDTH
        self.POS= (self.X, self.Y)

        if self.Y > MAX_HEIGHT:
            self.Y = -self.SCREEN.get_rect().height
        elif self.Y < MIN_HEIGHT -self.SCREEN.get_rect().height:
            self.Y = MAX_HEIGHT
        self.POS = (self.X,self.Y)

    def moveBoxWrap(self, KEYPRESSES, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH = 0, MIN_HEIGHT =0):
        self.moveBox(KEYPRESSES)
        self.wrapBox(MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH = 0, MIN_HEIGHT =0)


    # --- ACCESSOR METHODS --- #

    def getBox(self):
        return self.SCREEN

    def getPOS(self):
        return self.POS


if __name__ == "__main__":
    import sys
    from random import randrange
    pygame.init()
    WINDOW = Window()
    WINDOW.setBackgroundColor(Color.BLACK)
    #WHITE_BOX = Box(50,50)
    BOXES = []
    for i in range(100):
        SIZE = randrange(2,10)
        BOXES.append(Box(SIZE,SIZE, randrange(WINDOW.getVirtualWidth()), randrange(WINDOW.getVirtualHeight())))


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        KEY_PRESSES = pygame.key.get_pressed()
        for i in range(100):
            BOXES[i].moveBoxWrap(KEY_PRESSES, WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())
        #WHITE_BOX.moveBoxChkBoundaries(KEY_PRESSES, WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())
        #WHITE_BOX.moveBoxWrap(KEY_PRESSES, WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        #OUPUTS
        WINDOW.clearScreen()
        for i in range(100):
            WINDOW.getScreen().blit(BOXES[i].getBox(), BOXES[i].getPOS())
        #WINDOW.getScreen().blit(WHITE_BOX.getBox(), WHITE_BOX.getPOS())
        WINDOW.updateFrame()


