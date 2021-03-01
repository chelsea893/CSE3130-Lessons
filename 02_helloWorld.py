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

# --- Modifier Methods --- #
    def updateFrame(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    def clearFrame(self):
        self.SCREEN.fill(self.BACKGROUND)
# --- Accessor Methods --- #
    def getScreen(self):
        return self.SCREEN

    def getVirtualWidth(self):
        return self.SCREEN.get_rect().width

    def getVirtualHeight(self):
        return self.SCREEN.get_rect().height

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
        self.DIR_X = 1
        self.SPEED = 5
        self.DIR_Y = 1
    # --- Modifier Methods (Setter) --- #
    def horizBounce(self, SCREEN):
        self.X = self.X + self.DIR_X*self.SPEED
        if self.X > SCREEN.getVirtualWidth() - self.getTextWidth():
            self.DIR_X = -1
            self.SPEED = self.SPEED + 0.4
            self.SCREEN = self.FONT.render(self.TEXT, True, Color.BLUE)
            self.FONT = pygame.font.SysFont("Arial", 50)
        if self.X < 0:
            self.DIR_X = 1
            self.SPEED = self.SPEED + 0.4
            self.SCREEN = self.FONT.render(self.TEXT, True, Color.GREEN)

        self.POS = (self.X, self.Y)

    def vertBounce(self, SCREEN):
        self.Y = self.Y + self.DIR_Y*self.SPEED
        if self.Y > SCREEN.getVirtualHeight() - self.getTextHeight():
            self.DIR_Y = -1
            self.SCREEN = self.FONT.render(self.TEXT, True, Color.RED)
            self.FONT = pygame.font.SysFont("Arial", 30)
        if self.Y < 0:
            self.DIR_Y = 1
            self.SCREEN = self.FONT.render(self.TEXT, True, Color.WHITE)

        self.POS = (self.X, self.Y)

    # --- Accessor Methods (Getter) --- #

    def getText(self):
        return self.SCREEN

    def getPOS(self):
        return self.POS

    def getTextWidth(self):
        return self.SCREEN.get_rect().width

    def getTextHeight(self):
        return self.SCREEN.get_rect().height

# --- MAIN PROGRAM CODE --- #

if __name__ == "__main__":
    import sys
    pygame.init()
    RUNNING = True

    WINDOW = Window()
    TEXT1 = Text("Hello World", 100, 130)
    TEXT2 = Text("Hi", 0, 0)

    while RUNNING:
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                sys.exit()

        # Processing
        TEXT1.horizBounce(WINDOW)
        TEXT1.vertBounce(WINDOW)
        TEXT2.horizBounce(WINDOW)
        TEXT2.vertBounce(WINDOW)

        #OUTPUTS
        WINDOW.clearFrame()
        WINDOW.getScreen().blit(TEXT1.getText(), TEXT1.getPOS())
        WINDOW.getScreen().blit(TEXT2.getText(), TEXT2.getPOS())
        WINDOW.updateFrame()
