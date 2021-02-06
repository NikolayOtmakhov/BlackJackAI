import game_cards
import game_background
import game_buttons
import game_player_selector
import game_render_log

class Drawables:
    def __init__(self,mem ,game, functions, ai):
        
        # All items must be a subclass of -> Drawable
        self.player_select = game_player_selector.Select(game)
        self.render_log = game_render_log.Text(game)
        self.background = game_background.Background(game)
        self.buttons = game_buttons.Buttons(mem, game, functions, ai)
        self.cards = game_cards.Cards(game)
        

    def get_list(self):
        return  [self.player_select
                ,self.render_log
                ,self.background
                ,self.buttons
                ,self.cards
                ]