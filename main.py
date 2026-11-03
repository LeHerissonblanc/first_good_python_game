import pyray as pr
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = pr.RAYWHITE

pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Game?")
pr.set_target_fps(60)

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT )

while not pr.window_should_close():

    dt = pr.get_frame_time()
    
    game.update(dt)
    game.draw(BG_COLOR)

pr.close_window()