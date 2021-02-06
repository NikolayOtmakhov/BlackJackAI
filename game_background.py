from drawable_item import Drawable
import pygame

class Background(Drawable):
    def __init__(self,game):
        self.line_color = (255,255,255)
        self.first_line_y_pos = 0.099
        self.line_seperation = 0.15
        self.number_of_lines = 7
        self.line_y_pos = self.first_line_y_pos
        self.game = game

    def draw(self, screen, size):
        
        self.line_y_pos2 = self.line_y_pos 
        for _ in range(self.number_of_lines):
            pygame.draw.line(screen, self.line_color, 
            (0, int(size[1]*self.line_y_pos2)), 
            (int(size[0]), int(size[1]*self.line_y_pos2)))
            self.line_y_pos2 += self.line_seperation 
        
        # left line
        pygame.draw.line(screen, self.line_color, 
            (0, 0), 
            (0, size[1]))
        
        #right line
        pygame.draw.line(screen, self.line_color, 
            (size[0]-1, 0), 
            (size[0]-1, size[1]))
        

        