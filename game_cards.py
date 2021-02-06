from drawable_item import Drawable
import pygame
import card
import pygame.gfxdraw

class Cards(Drawable):     

    def card_width_ratio(self,card_img):
        self.card_image_size = card_img.get_rect().size
        self.ratio = self.card_image_size[0]/self.card_image_size[1]
        return self.ratio
    
    def set_image(self, screen, img, left_top_cornet_position = (300,300), card_hight = 100):
        # transform image into desired hight
        self.card_image_adjusted = pygame.transform.scale(img, 
                ((int(self.card_width_ratio(img)*card_hight),int(card_hight))))                        
        screen.blit(self.card_image_adjusted,((int(left_top_cornet_position[0]),int(left_top_cornet_position[1]))))

    
    def draw_regular_cards(self,screen,size):
        self.card_y = 0.114 + 0.15 * 5
        for current_player in self.game.players.players:
            self.card_x = 0.02
            for selected_card in current_player.cards.loc["Main_Hand"].dropna():
                self.card_image = pygame.image.load(selected_card.img_loc)
                self.set_image(screen, self.card_image, (int(size[0]*self.card_x),int(size[1]*self.card_y)),int(size[1]*0.12))
                self.card_x += 0.07 
                if current_player == self.game.get_current_player():
                    self.x_2=self.card_x
                    self.y_2=self.card_y
                    self.dealer_playing = False
                if self.game.player_turn == len(self.game.players.players):
                    self.dealer_playing = True
            self.card_y -= 0.15   
        # Total of cards for current player         
        if not self.dealer_playing:
            font = pygame.font.SysFont(None, int(size[1]*0.12*0.3))
            current_count = self.game.get_current_player().card_value_total()
            text = font.render(f"Total: {current_count}", True, (255,255,255))
            if self.game.get_current_player().round_status.at['Main_Hand',"Status"] == "Playing":
                text_rect = text.get_rect(center=(size[0]*self.x_2 + int(size[0]*0.025), size[1]*self.y_2 + int(int(size[1]*0.016))))
                screen.blit(text, text_rect)


    def draw_dealer_cards(self,screen,size):
        self.card_y = 0.114 
        self.card_x = 0.02
        self.dealer_card_hidden = self.game.dealer_card_hidden
        self.card_number = 0
        for selected_card in self.game.players.dealer.cards.loc["Main_Hand"].dropna():
            if not (self.card_number == 0 and self.dealer_card_hidden):
                self.card_image = pygame.image.load(selected_card.img_loc)
            else:
                self.card_image = pygame.image.load(card.CardBack().img_loc)
            self.set_image(screen, self.card_image, (int(size[0]*self.card_x),int(size[1]*self.card_y)),int(size[1]*0.12))
            self.card_number += 1
            self.card_x += 0.07 
        self.card_y -= 0.15

    def draw_split_cards(self,screen,size):
        self.card_y = 0.114 + 0.15 * 5
        for current_player in self.game.players.players:
            self.card_x = 0.93
            for selected_card in current_player.cards.loc["Split_Hand"].dropna():
                self.card_image = pygame.image.load(selected_card.img_loc)
                self.set_image(screen, self.card_image, (int(size[0]*self.card_x),int(size[1]*self.card_y)),int(size[1]*0.12))
                self.card_x -= 0.07 
            if current_player == self.game.get_current_player():
                self.x_2=self.card_x
                self.y_2=self.card_y
                self.dealer_playing = False
            if self.game.player_turn == len(self.game.players.players):
                self.dealer_playing = True
            self.card_y -= 0.15
        # Total of cards for current player         
        if not self.dealer_playing:
            font = pygame.font.SysFont(None, int(size[1]*0.12*0.3))
            current_count = self.game.get_current_player().card_value_total("Split_Hand")
            text = font.render(f"Total: {current_count}", True, (255,255,255))
            if self.game.get_current_player().round_status.at['Main_Hand',"Status"] != "Playing":
                text_rect = text.get_rect(center=(size[0]*self.x_2 + int(size[0]*0.025), size[1]*self.y_2 + int(int(size[1]*0.016))))
                screen.blit(text, text_rect)

    def __init__(self, game):
        self.game = game
    
    def draw(self, screen, size):
        self.draw_regular_cards(screen, size)
        self.draw_dealer_cards(screen, size)
        self.draw_split_cards(screen, size)




