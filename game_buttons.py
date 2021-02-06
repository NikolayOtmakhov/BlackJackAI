from drawable_item import Drawable
import pandas as pd
import numpy as np
import pygame
import button
import ai

class Buttons(Drawable):

    #placeholder
    def ph(self):
        pass

    def __init__(self, memory, game, functions, ai):

        self.mem = memory

        self.button_color = (0,0,0)
        self.button_selection_color = (100,0,0)
    
        self.hit = functions.hit 
        self.stand = functions.stand
        self.dd = functions.double_down
        self.nr = functions.next_round
        self.sp = functions.split
        self.sp = functions.split
        self.ai = ai.action

        self.btn_df = pd.DataFrame(columns = ["Button_Name", "Button_Text", "Function"  , "Allowed", "Visible", "X_Loc" ] )
        self.btn_df.loc[len(self.btn_df)] =( ["Cont_Button", "Continue"   , self.nr     , True     , True     , None    ] )
        self.btn_df.loc[len(self.btn_df)] =( ["Hit_Button" , "Hit"        , self.hit    , True     , True     , None    ] )
        self.btn_df.loc[len(self.btn_df)] =( ["Stand"      , "Stand"      , self.stand  , True     , True     , None    ] )
        self.btn_df.loc[len(self.btn_df)] =( ["Double_Down", "Double Down", self.dd     , True     , True     , None    ] )
        self.btn_df.loc[len(self.btn_df)] =( ["Split"      , "Split"      , self.sp     , True     , True     , None    ] )
        self.btn_df.loc[len(self.btn_df)] =( ["Surrender"  , "Surrender"  , self.ph     , False    , True     , None    ] )
        self.btn_df.loc[len(self.btn_df)] =( ["Insurance"  , "Insurance"  , self.ph     , False    , True     , None    ] )
        self.btn_df.loc[len(self.btn_df)] =( ["Info"       , "Open Info"  , self.ph     , False    , True     , None    ] )
        self.btn_df.loc[len(self.btn_df)] =( ["AI"         , "AI"         , self.ai     , True     , True     , None    ] )

        self.btn_df = self.btn_df.set_index("Button_Name").rename_axis(None)

    def draw(self,screen, size):
        self.number_of_buttons = self.btn_df[self.btn_df["Visible"]==True].shape[0]
        self.botton_width = int(size[0] / self.number_of_buttons)
        self.btn_df_visible = self.btn_df[self.btn_df["Visible"]==True]
        self.btn_df_visible["X_Loc"] = np.linspace(0,size[0],self.number_of_buttons,endpoint=False).astype(int) 
        self.btn_creator = button.Button(self.mem)
        for btn_name, btn in self.btn_df_visible.iterrows():
            if self.btn_df.at[btn_name,"Allowed"] == True:
                self.text_c = (255,255,255)
            else:
                self.text_c = (25,25,25)
            self.mouse_x_pos, self.mouse_y_pos = pygame.mouse.get_pos()
            self.btn_creator.create(screen,self.mouse_x_pos,self.mouse_y_pos,btn["Function"],btn["Button_Text"],btn["X_Loc"],0,self.botton_width,size[1]*0.099,
            no_hover_button_color=self.button_color,hover_button_color=self.button_selection_color,hover_text_color=self.text_c,no_hover_text_color= self.text_c,
            border=True,text_relative_font_size=0.25)

