'''
title: text object
'''

from loader import Color
import pygame
from mySprite import MySprite

class Text(MySprite):
    def __init__(self, TEXT = "Hello World", COLOR = Color.WHITE):
        super().__init__()
        self.TEXT = TEXT
        self.COLOR = COLOR
        self.FONT = pygame.font.SysFont("Arial", 36)
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOR)

    def setText(self, NEW_TEXT):
        self.TEXT = NEW_TEXT
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOR)



if __name__ == "__main__":
    import sys
    from window import Window

    pygame.init()

    WINDOW = Window()
    TEXT1 = Text()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WINDOW.getScreen().blit(TEXT1.getScreen(), TEXT1.getPOS())
        WINDOW.updateFrame()


