import pyray as pr  # type: ignore
from entity.player import Player
from entity.entity import State


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.entities = []

        self.player = Player(
            x= 0,
            y= 0,
            height= 20,
            speed= 200,
        )
        self.entities.append(self.player)

        self.camera = pr.Camera2D()
        self.camera.target = pr.Vector2(self.player.position.x, self.player.position.y)
        self.camera.offset = pr.Vector2(
            self.screen_width / 2,
            self.screen_height / 2,
        )
        self.camera.rotation = 0
        self.camera.zoom = 1

    def update(self, dt: float):
        for entity in self.entities:
            entity.update(dt)
        
        # follow the player
        self.camera.target = pr.Vector2(self.player.position.x, self.player.position.y)

    def draw(self, bg_color):
        
        pr.begin_drawing()
        
        pr.clear_background(bg_color)

        pr.begin_mode_2d(self.camera)
        
        # Grille du monde
        for x in range(-5000, 5001, 50):
            pr.draw_line(x, -5000, x, 5000, pr.LIGHTGRAY)

        for y in range(-5000, 5001, 50):
            pr.draw_line(-5000, y, 5000, y, pr.LIGHTGRAY)
        
        for entity in self.entities:
            entity.draw()
            
        pr.end_mode_2d()

        pr.draw_text("Game?", 10, 10, 20, pr.RED)
        pr.draw_text(f"player x: {self.player.position.x:.2f}", 10, 30, 20, pr.RED)
        pr.draw_text(f"player y: {self.player.position.y:.2f}", 10, 50, 20, pr.RED)
        pr.draw_text(f"player speed: {self.player.speed}", 10, 70, 20, pr.RED)
        pr.draw_text(f"player temp speed: {self.player.temp_speed}", 10, 90, 20, pr.RED)

        pr.end_drawing()