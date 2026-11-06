import pyray as pr
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = pr.RAYWHITE
FPS = 60

def main():
    pr.set_config_flags(pr.FLAG_MSAA_4X_HINT | pr.FLAG_VSYNC_HINT) # type: ignore
    pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Game?")
    # pr.set_target_fps(FPS)  # VSync enabled

    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, cell_size=50)

    while not pr.window_should_close():
        dt = pr.get_frame_time()
        game.update(dt)
        game.draw(dt, BG_COLOR)

    pr.close_window()

if __name__ == "__main__":
    main()