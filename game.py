import pyray as pr  # type: ignore
from entity.player import Player
from entity.entity import Entity, State, Shape

class Game:
    
    def draw_gui(self, dt):
        pr.draw_text("Game?", 10, 10, 20, pr.RED)
        pr.draw_text(f"player x: {self.player.position.x:.2f}", 10, 30, 20, pr.RED)
        pr.draw_text(f"player y: {self.player.position.y:.2f}", 10, 50, 20, pr.RED)
        pr.draw_text(f"player speed: {self.player.speed}", 10, 70, 20, pr.RED)
        pr.draw_text(f"player temp speed: {self.player.temp_speed}", 10, 90, 20, pr.RED)
        pr.draw_text(f"dt: {dt}", 10, 110, 20, pr.RED)
    
    def __init__(self, screen_width, screen_height, cell_size = 50):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size

        # init all entities
        self.entities = []

        self.player = Player(
            x= 0,
            y= 0,
            size= pr.Vector2(30,30),
            color= pr.SKYBLUE,
            speed= 200,
        )
        self.entities.append(self.player)
        
        self.box = Entity(
            x= cell_size * 2,
            y= cell_size * 3,
            size= pr.Vector2(self.cell_size*10, self.cell_size*5),
            color= pr.DARKGRAY,
            shape= Shape.RECT,
            state= State.STATIC
        )
        self.entities.append(self.box)


        # camera
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
            if not entity == self.player:
                entity.update(dt)
            
        old_x = self.player.position.x
        old_y = self.player.position.y

        self.player.update(dt)

        new_x = self.player.position.x
        new_y = self.player.position.y
        radius = self.player.size.x / 2

        # first: x collision ; second: y collision
        for obstacle in self.entities:
            if obstacle is self.player or obstacle.state != State.STATIC:
                continue

            obstacle_rect = pr.Rectangle(
                obstacle.position.x,
                obstacle.position.y,
                obstacle.size.x,
                obstacle.size.y,
            )

            # x move
            if pr.check_collision_circle_rec(
                pr.Vector2(new_x, old_y),
                radius,
                obstacle_rect,
            ):
                new_x = old_x

            # y move
            if pr.check_collision_circle_rec(
                pr.Vector2(new_x, new_y),
                radius,
                obstacle_rect,
            ):
                new_y = old_y

        self.player.position.x = new_x
        self.player.position.y = new_y
        
        # follow the player
        self.camera.target = pr.Vector2(self.player.position.x, self.player.position.y)

    def draw(self, dt, bg_color):
        
        pr.begin_drawing()
        
        pr.clear_background(bg_color)

        pr.begin_mode_2d(self.camera)
        
        # World grid
        for x in range(-5000, 5001, self.cell_size):
            pr.draw_line(x, -5000, x, 5000, pr.LIGHTGRAY)
        for y in range(-5000, 5001, self.cell_size):
            pr.draw_line(-5000, y, 5000, y, pr.LIGHTGRAY)
        pr.draw_rectangle_lines(-5000, -5000, 10_000, 10_000, pr.RED)
        
        for entity in self.entities:
            entity.draw()
            
        pr.end_mode_2d()

        self.draw_gui(dt)

        pr.end_drawing()