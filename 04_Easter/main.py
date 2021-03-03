'''
title: Easter Bunny Egg Hunt
author: Chelsea Chen
date-created: 2021-03-03
'''

import pygame
from window import Window
from text import Text
from box import Box
from loader import Color

if  __name__ == "__main__":
    import sys
    pygame.init()
    WINDOW = Window()
    TEXT = Text("RED")
    RED_BOX = Box(50,50,WINDOW.getVirtualWidth()//2 - 25, WINDOW.getVirtualHeight()//2 -25, Color.RED)
    TEXT.setPOS(RED_BOX.getX(), RED_BOX.getY()- TEXT.getHeight())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        KEYS_PRESSED = pygame.key.get_pressed()
        RED_BOX.wasdMove(KEYS_PRESSED)
        TEXT.wasdMove(KEYS_PRESSED)

        WINDOW.getScreen().blit(RED_BOX.getScreen(), RED_BOX.getPOS())
        WINDOW.getScreen().blit(TEXT.getScreen(), TEXT.getPOS())
        WINDOW.updateFrame()

