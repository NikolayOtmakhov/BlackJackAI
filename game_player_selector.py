from drawable_item import Drawable
import pygame

class Select(Drawable):
    def __init__(self,game):
        self.line_color = (255,255,255)
        self.first_line_y_pos = 0.099
        self.line_seperation = 0.15
        self.number_of_lines = 7
        self.line_y_pos = self.first_line_y_pos
        self.game = game

    def draw(self, screen, size):
        player_selection_color = (100,0,0)
        player_number = self.game.player_turn + 1
        # selection line
        top = int(size[1] - self.line_seperation*size[1] * player_number)
        pygame.draw.rect(screen, player_selection_color,
            pygame.Rect(
                0 #x1
                ,top #y1
                ,size[0] #x2
                ,top + size[1]  #y2
            )
        ) 
        pygame.draw.rect(screen, (0,0,0),
            pygame.Rect(
                0 #x1
                ,top + self.line_seperation*size[1]  #y1
                ,size[0] #x2
                ,top + size[1] #y2
            )
        ) 
