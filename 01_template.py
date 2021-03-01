'''
title: Pygame template
author: Chelsea Chen
date-created: 2021-03-01
'''
import pygame
# run with compsciIA

class Window:
    '''
    Creates the Window that will load Pygame
    '''
    def __init__(self, TITLE, WIDTH, HEIGHT,FPS):
        self.TITLE = TITLE # text that appears in the title bar of the window
        self.FPS = FPS # Frames per second the program will run
        self.WIDTH = WIDTH # Width of the window
        self.HEIGHT = HEIGHT # Height of the window
        self.SCREEN_DIMENSIONS = (self.WIDTH, self.HEIGHT) #Window frame dimesions
        self.FRAME = pygame.time.Clock() # Loads Pygame's clock module to measure FPS
        self.SCREEN = pygame.display.set_mode(self.SCREEN_DIMENSIONS)
        self.SCREEN.fill((50,50,50)) # Fills the window with GREY colour
        self.CAPTION = pygame.display.set_caption(self.TITLE)

    def updateFrame(self):
        self.FRAME.tick(self.FPS) # Waits for the appropriate time to update the screen
        pygame.display.flip() # Update the display with the new frame

    def getScreen(self):
        return self.SCREEN

class Text:
    """
    creates a text object to be placed on a screen
    """
    def __init__(self, TEXT):
        self.TEXT = pygame.font.SysFont("Arial",36)
        self.SCREEN = self.TEXT.render(TEXT, 1, (255, 255, 255))
    def getText(self):
        return self.SCREEN
# PROGRAM CODE STARTS HERE

if __name__ == "__main__":
    import sys
    pygame.init()
    RUNNING = True

    WINDOW = Window("template", 640, 480, 30)
    TEXT = Text("Hello World")

    while RUNNING:
        for event in pygame.event.get():
            # Check if the red "x" button is clicked and stop the program
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                sys.exit()
        WINDOW.getScreen().blit(TEXT.getText(), (100,100)) #blit places the screen onto the display's screen
        WINDOW.updateFrame()

