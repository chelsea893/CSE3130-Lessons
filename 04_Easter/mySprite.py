'''
title: Abstract Sprite Class
author: Chelsea Chen
date-created: 2021-03-03
'''
import pygame
class MySprite:

    def __init__(self):
        self.WIDTH = 0
        self.HEIGHT = 0
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.SCREEN = None
        self.RECT = None
        self.X = 0
        self.Y = 0
        self.POS = (self.X, self.Y)
        self.SPEED = 5

    # --- MODIFIER METHODS --- #

    def setPOS(self,X, Y):
        self.X = X
        self.Y = Y
        self.updatePOS()

    def updatePOS(self):
        self.POS = (self.X, self.Y)

    def updateDimension(self):
        self.DIMENSION = (self.WIDTH, self.HEIGHT)

    ## Movement

    def wasdMove(self, KEYPRESSES):
        if KEYPRESSES[pygame.K_d] == 1:
            self.X = self.X + self.SPEED
        if KEYPRESSES[pygame.K_a] == 1:
            self.X = self.X -self.SPEED
        if KEYPRESSES[pygame.K_w] == 1:
            self.Y = self.Y -self.SPEED
        if KEYPRESSES[pygame.K_s] == 1:
            self.Y = self.Y + self.SPEED
        self.updatePOS()

    def checkBoundaries(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH = 0, MIN_HEIGHT = 0):
        if self.X > MAX_WIDTH - self.getWidth():
            self.X = MAX_WIDTH -self.getWidth()
        elif self.X < MIN_WIDTH:
            self.X = MIN_WIDTH
        if self.Y > MAX_HEIGHT - self.getHeight():
            self.Y = MAX_HEIGHT -self.getHeight()
        elif self.Y < MIN_HEIGHT:
            self.Y = MIN_HEIGHT

        self.updatePOS()

    def wasdMoveChkBoundaries(self, KEYPRESSES, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH = 0, MIN_HEIGHT = 0):
        self.wasdMove(KEYPRESSES)
        self.checkBoundaries(MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT)

    # --- ACCESSOR METHODS --- #




    # ---- ACCESSOR METHODS --- #

    def getScreen(self):
        return self.SCREEN

    def getPOS(self):
        return self.POS

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getWidth(self):
        return self.SCREEN.get_rect().width

    def getHeight(self):
        return self.SCREEN.get_rect().height

    def getRect(self):
        self.RECT = self.SCREEN.get_rect()
        self.RECT.x = self.X
        self.RECT.y = self.Y
        return self.RECT

