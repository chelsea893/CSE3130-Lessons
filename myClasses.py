"""
title: Custom Classes
author: Chelsea Chen
date-created: 2021-03-02
"""

import pygame

class Color:
    GREY = (100,100,100)
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    RED = (255, 0, 0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    MAGENTA = (255, 0, 255)

class Window:
    def __init__(self, TITLE = "Pygame", WIDTH =630, HEIGHT = 480, FPS = 30):
        self.TITLE = TITLE
        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCREEN_DIMESIONS = (self.WIDTH, self.HEIGHT)
        self.BACKGROUND = Color.GREY
        self.FRAME = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(self.SCREEN_DIMESIONS)
        self.SCREEN.fill(self.BACKGROUND)
        self.CAPTION = pygame.display.set_caption(self.TITLE)

    # --- MODIFIER METHODS (SETTER) --- #

    def updateFrame(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    def clearScreen(self):
        self.SCREEN.fill(self.BACKGROUND)

    def setBackgroundColor(self,COLOR):
        self.BACKGROUND = COLOR
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