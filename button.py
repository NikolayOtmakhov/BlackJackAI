import pygame

class Button():

    def __init__(self, memory):
        self.mem = memory

    def create(self,screen,mouse_x_pos,mouse_y_pos
                ,button_function,button_text
                ,button_x_pos,button_y_pos,button_width
                ,button_height,hover_button_color=(255,255,255)
                ,no_hover_button_color=(100,0,0)
                ,hover_text_color=(0,0,0)
                ,no_hover_text_color=(255,255,255)
                ,text_relative_font_size=0.5
                ,font=None,border=False
                ,border_color=(255,255,255)
                ,hover = True, clickable = True):

        mouse_x_pos, mouse_y_pos, button_x_pos, button_y_pos, button_width, button_height = \
            int(mouse_x_pos), int(mouse_y_pos), int(button_x_pos), int(button_y_pos), int(button_width), int(button_height)
            
        
        button = pygame.Rect(button_x_pos, button_y_pos, button_width, button_height)

        if hover == False:
            hover_button_color = no_hover_button_color
            hover_text_color = no_hover_text_color

        font = pygame.font.SysFont(font, int(button_height*text_relative_font_size))

        if (button_x_pos + button_width > mouse_x_pos > button_x_pos and button_y_pos + button_height > mouse_y_pos > button_y_pos):
            pygame.draw.rect(screen, hover_button_color,(button_x_pos,button_y_pos,button_width,button_height))
            text = font.render(button_text, True, hover_text_color)
        else:
            pygame.draw.rect(screen, no_hover_button_color,(button_x_pos,button_y_pos,button_width,button_height))
            text = font.render(button_text, True, no_hover_text_color)

        text_rect = text.get_rect(center=(button_x_pos + int(button_width/2), button_y_pos + int(button_height/2)))

        if border == True:
            pygame.draw.rect(screen, border_color, (button_x_pos, button_y_pos, button_width, button_height), 3)

        screen.blit(text, text_rect)
        clicked = self.mem
        if clickable:
            if button.collidepoint((mouse_x_pos, mouse_y_pos)):
                if clicked.mouse_click_state:
                    button_function()
