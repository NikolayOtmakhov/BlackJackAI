from drawable_item import Drawable
import pygame

class Text(Drawable):


    def __init__(self, game):
        self.game = game
        
    def draw(self,screen, size):
        # self.text = self.game.text
        # for i, l in enumerate(self.text):
        #     font = pygame.font.SysFont(None, 20)
        #     text = font.render(f"{l}", True, (255,255,255))
        #     text_rect = text.get_rect(topleft=(size[0] + int(size[0]*0.02), 20 + 20*i))
        #     screen.blit(text, text_rect)
        pass