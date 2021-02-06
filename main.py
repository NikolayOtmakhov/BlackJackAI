import memory

import graphics
import game_drawables
import game_logic
import game_functions
import ai

def main():
    mem = memory.Variables()
    game = game_logic.BlackJack(mem)
    functions = game_functions.Functions(mem, game)
    AI = ai.AI(mem, game, functions)
    drawables = game_drawables.Drawables(mem, game, functions, AI)
    disp = graphics.Display(mem)
    while True:
        disp.update(drawables.get_list())

if __name__ == "__main__":
    main()


