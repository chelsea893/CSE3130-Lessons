'''
title: Hello World
author: Chelsea Chen
date-created: 2021-03-01
'''

import pygame

class Color:
    WHITE = (255, 255, 255)
    GREY = (50,50,50)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

class Window:
    '''
    Create the window that will load Pygame
    '''
    def __init__(self, TITLE = "Pygame Game", WIDTH = 640, HEIGHT = 480, FPS = 30):
        self.TITLE = TITLE
        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCREEN_DIMENSIONS = (self.WIDTH, self.HEIGHT)
        self.FRAME = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(self.SCREEN_DIMENSIONS)
        self.BACKGROUND = Color.GREY
        self.SCREEN.fill(self.BACKGROUND)
        self.CAPTION = pygame.display.set_caption(self.TITLE)


    def updateFrame(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    def getScreen(self):
        return self.SCREEN

class Text:
    """
    Creates a text object and manipulates it
    """

    def __init__(self, TEXT, x=0, y=0):
        self.TEXT = TEXT
        self.FONT = pygame.font.SysFont("Arial", 36)
        self.SCREEN = self.FONT.render(self.TEXT, True, Color.WHITE)
        self.X = x
        self.Y = y
        self.POS = (self.X, self.Y)

    # --- Accessor Methods (Getter) --- #

    def getText(self):
        return self.SCREEN

    def getPOS(self):
        return self.POS

# --- MAIN PROGRAM CODE --- #

if __name__ == "__main__":
    import sys
    pygame.init()
    RUNNING = True

    WINDOW = Window()
    TEXT1 = Text("Hello World")

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                sys.exit()
        WINDOW.getScreen().blit(TEXT1.getText(), TEXT1.getPOS())
        WINDOW.updateFrame()
