'''
title: The Game Engine
'''
# This puts all the pieces together.

import pygame
import sys
from random import randrange
from window import Window
from imageSprite import ImageSprite
from loader import Image
from text import Text
from loader import Color

class Game:

    pygame.init()

    def __init__(self):
        ## Setup
        self.WINDOW = Window()
        self.WINDOW.setBackgroundImage(Image.BACKGROUND)
        self.PLAYER = ImageSprite(Image.PLAYER)
        self.PLAYER.setScale(2)
        self.PLAYER.setPOS((self.WINDOW.getVirtualWidth() - self.PLAYER.getWidth())//2, (self.WINDOW.getVirtualHeight()-self.PLAYER.getHeight())//2)
        self.SHRUBS = []
        for i in range(5):
            self.SHRUBS.append(ImageSprite(Image.SHRUB))
            self.SHRUBS[-1].setScale(5)
        self.EGGS = []
        for i in range(2):
            for egg in Image.EGGS:
                self.EGGS.append(ImageSprite(egg))
                self.EGGS[-1].setScale(3)
                self.placeItems()
        self.SCORE = 0
        self.SCORE_TEXT = Text(f"SCORE: {self.SCORE}")
        # Timer
        self.TIMER = pygame.time.Clock()
        self.TIMER_MS = 0
        self.TIME_LEFT = 15
        self.TIME_TEXT = Text(f"TIME LEFT: {self.TIME_LEFT}")
        self.TIME_TEXT.setPOS(self.WINDOW.getVirtualWidth()-self.TIME_TEXT.getWidth(), 0)
        # Start Screen
        self.START_TEXT = Text("WELCOME TO EASTER HUNT! COLLECT AS MANY EGGS YOU CAN!")
        self.START_TEXT.setScale(2)
        self.START_TEXT.setPOS(self.WINDOW.getVirtualWidth()//2 - self.START_TEXT.getWidth()//2, (self.WINDOW.getVirtualHeight()-self.START_TEXT.getHeight())//2)
        self.START = Text("PRESS s/S to start")
        self.START.setScale(2)
        self.START.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.START.getWidth() // 2,
                               (self.WINDOW.getVirtualHeight() - self.START.getHeight() + 100) // 2)

        self.START_GAME = False

        # End screen
        self.END = Text("TIME HAS RUN OUT")
        self.END.setPOS(self.WINDOW.getVirtualWidth()//2 - self.END.getWidth()//2, (self.WINDOW.getVirtualHeight()-self.END.getHeight())//2)

        self.SCORE_END = Text(f"Your Score was: {self.SCORE}")
        self.SCORE_END.setPOS(self.WINDOW.getVirtualWidth()//2 - self.SCORE_END.getWidth()//2,(self.WINDOW.getVirtualHeight()- self.SCORE_END.getHeight() + self.END.getHeight() + 100)//2)



    def start(self, KEYPRESSES):
        if KEYPRESSES[pygame.K_s] == 1:
            self.START_GAME = True


    def placeItems(self):
        for shrub in self.SHRUBS:
            shrub.setPOS(randrange(self.WINDOW.getVirtualWidth()-shrub.getWidth()), randrange(self.WINDOW.getVirtualHeight()-shrub.getHeight()))
        for egg in self.EGGS:
            egg.setPOS(randrange(self.WINDOW.getVirtualWidth()-egg.getWidth()), randrange(self.WINDOW.getVirtualHeight()-egg.getHeight()))

    def getSpriteCollision(self, SPRITE1, SPRITE2):
        if pygame.Rect.colliderect(SPRITE1.getRect(), SPRITE2.getRect()):
            return True
        else:
            return False

    def checkEggPicked(self):
        PICKED = 0
        for egg in self.EGGS:
            if egg.getX() == self.WINDOW.getVirtualWidth():
                PICKED += 1
        if PICKED == len(self.EGGS):
            return True
        else:
            return False

    def checkTime(self):
        if self.TIME_LEFT == 0:
            return True
        else:
            return False

    def updateTime(self):
        self.TIMER_MS += self.TIMER.tick()
        if self.TIMER_MS > 1000 and self.TIME_LEFT > 0:
            self.TIME_LEFT -= 1
            self.TIME_TEXT.setText(f"TIME LEFT: {self.TIME_LEFT}")
            self.TIMER_MS = 0

    def run(self):
        while True:
            ## -- INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            KEYS_PRESSED = pygame.key.get_pressed()
            self.WINDOW.updateFrame()
            self.WINDOW.getScreen().blit(self.START_TEXT.getScreen(), self.START_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.START.getScreen(), self.START.getPOS())
            self.start(KEYS_PRESSED)
            if self.START_GAME == True:
                ## -- PROCESSING
                KEYS_PRESS = pygame.key.get_pressed()
                self.PLAYER.wasdMoveChkBoundaries(KEYS_PRESS, self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())

                for egg in self.EGGS:
                    if self.getSpriteCollision(self.PLAYER, egg):
                        egg.setPOS(self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())
                        self.SCORE += 1
                        self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}"s)

                if self.checkEggPicked():
                    self.placeItems()

                self.updateTime()





                ## -- OUTPUTS

                self.WINDOW.clearScreen()
                self.WINDOW.getScreen().blit(self.PLAYER.getScreen(), self.PLAYER.getPOS())
                for egg in self.EGGS:
                    self.WINDOW.getScreen().blit(egg.getScreen(), egg.getPOS())
                for shrub in self.SHRUBS:
                    self.WINDOW.getScreen().blit(shrub.getScreen(), shrub.getPOS())
                self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
                self.WINDOW.getScreen().blit(self.TIME_TEXT.getScreen(), self.TIME_TEXT.getPOS())
                if self.checkTime():
                    self.WINDOW.clearScreen()
                    self.WINDOW.getScreen().blit(self.END.getScreen(), self.END.getPOS())
                    self.WINDOW.getScreen().blit(self.SCORE_END.getScreen(), self.SCORE_END.getPOS())


                self.WINDOW.updateFrame()

if __name__ == "__main__":
    GAME = Game()
    GAME.run()
