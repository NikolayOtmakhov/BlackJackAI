import pygame
import sys
from pygame.locals import *

class Display:
    def __init__(self, memory):
        pygame.init()
        print("ttttttt")
        self.size = [1280, 720]
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        # For global click state
        self.mem = memory

    # listener for alt f4
    def is_trying_to_quit(self, event: object):
        pressed_keys = pygame.key.get_pressed()
        alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
        x_button = event.type == pygame.QUIT
        altF4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4
        return x_button or altF4

    # checker for quit event
    def allow_hard_quit(self, event: object) -> None:
        hard_quit = bool(self.is_trying_to_quit(event))
        if hard_quit == True:
            pygame.quit()
            sys.exit()

    # main graphics/event loop
    def update(self,drawables):
        self.screen.fill((0,0,0))
        clicked = self.mem
        clicked.mouse_click_state = False
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            self.allow_hard_quit(event)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked.mouse_click_state = True
            if event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(
                    event.dict['size'],  RESIZABLE)
            if event.type == pygame.QUIT: sys.exit()
        for obj in drawables:
            obj.draw(self.screen,self.screen.get_size())

        # pygame.display.update()
        pygame.display.flip()