"""
title: Custom Classes
author: Chelsea Chen
date-created: 2021-03-02
"""

import pygame
from loader import Color
from imageSprite import ImageSprite


class Window:
    def __init__(self, TITLE = "Pygame", WIDTH =630, HEIGHT = 480, FPS = 30):
        self.TITLE = TITLE
        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCREEN_DIMESIONS = (self.WIDTH, self.HEIGHT)
        self.BACKGROUND = Color.GREY
        self.BACKGROUND_IMAGE = None
        self.FRAME = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(self.SCREEN_DIMESIONS)
        self.SCREEN.fill(self.BACKGROUND)
        self.CAPTION = pygame.display.set_caption(self.TITLE)

    # --- MODIFIER METHODS (SETTER) --- #

    def updateFrame(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    def clearScreen(self):
        if self.BACKGROUND_IMAGE is None:
            self.SCREEN.fill(self.BACKGROUND)
        else:
            self.SCREEN.blit(self.BACKGROUND_IMAGE.getScreen(), self.BACKGROUND_IMAGE.getPOS())

    def setBackgroundColor(self,COLOR):
        self.BACKGROUND = COLOR
        self.clearScreen()

    def setBackgroundImage(self, IMAGE_FILE):
        self.BACKGROUND_IMAGE = ImageSprite(IMAGE_FILE)
        ## Scale the image to fit the windwo
        if self.BACKGROUND_IMAGE.getWidth() < self.getVirtualWidth():
            self.BACKGROUND_IMAGE.setScale(self.BACKGROUND_IMAGE.getWidth()/self.getVirtualWidth())
        if self.BACKGROUND_IMAGE.getHeight() < self.getVirtualHeight():
            self.BACGROUND_IMAGE.setScale(self.BACKGROUND_IMAGE.getHeight()/self.getVirtualHeight())
        self.clearScreen()


    # --- ACCESSOR METHODS (GETTER) --- #

    def getScreen(self):
        return self.SCREEN

    def getVirtualWidth(self):
        return self.SCREEN.get_rect().width

    def getVirtualHeight(self):
        return self.SCREEN.get_rect().height


if __name__ == "__main__":
    import sys
    pygame.init()
    WINDOW = Window()
    WINDOW.setBackgroundColor(Color.RED)
    RUNNING = True

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                sys.exit()

        WINDOW.updateFrame()