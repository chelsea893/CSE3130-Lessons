'''
Title: The Game Engine
'''
# This puts all the pieces together

import pygame
import sys
from random import randrange
from window import Window
from imageSprite import ImageSprite
from loader import Image
from text import Text
pygame.init()
class Game:
    pygame.init()
    def __init__(self):
        pygame.init()
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
        for egg in Image.EGGS:
            self.EGGS.append(ImageSprite(egg))
            self.EGGS[-1].setScale(3)
            self.placeItems()
        self.SCORE = 0
        self.SCORE_TEXT = Text(f"Score: {self.SCORE}")
        #Timer
        self.TIMER = pygame.time.Clock()
        self.TIMER_MS = 0
        self.TIME_LEFT = 15
        self.TIME_TEXT = Text(f"TIME LEFT: {self.TIME_LEFT}")
        self.TIME_TEXT.setPOS(self.WINDOW.getVirtualWidth()-self.TIME_TEXT.getWidth(), 0)


    def placeItems(self):
        for shrub in self.SHRUBS:
            shrub.setPOS(randrange(self.WINDOW.getVirtualWidth()-shrub.getWidth()), randrange(self.WINDOW.getVirtualHeight()-shrub.getHeight()))

        for egg in self.EGGS:
            egg.setPOS(randrange(self.WINDOW.getVirtualWidth() -egg.getWidth()), randrange(self.WINDOW.getVirtualHeight()-egg.getHeight()))

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
            ## -- PROCESSING
            self.PLAYER.wasdMove(KEYS_PRESSED)
            for egg in self.EGGS:
                if self.getSpriteCollision(self.PLAYER,egg):
                    egg.setPOS(self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())
                    self.SCORE += 1
                    self.SCORE_TEXT.setText(f"SCORE: {self.SCORE}")

            if self.checkEggPicked():
                self.placeItems()



            ## -- OUTPUTS
            self.WINDOW.clearScreen()
            self.WINDOW.getScreen().blit(self.PLAYER.getScreen(), self.PLAYER.getPOS())
            for egg in self.EGGS:
                self.WINDOW.getScreen().blit(egg.getScreen(), egg.getPOS())
            for shrub in self.SHRUBS: # want to be in front
                self.WINDOW.getScreen().blit(shrub.getScreen(), shrub.getPOS())
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.TIME_TEXT.getScreen())
            self.WINDOW.updateFrame()


if __name__ == "__main__":
    GAME = Game()
    GAME.run()

