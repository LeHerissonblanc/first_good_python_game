import pyray as pr
from entity.entity import Entity

class Player(Entity):
    def update(self, dt: float):
        super().update(dt)
        if pr.is_key_down(pr.KEY_D):self.velocity_x += self.SPEED * dt # type: ignore
        if pr.is_key_down(pr.KEY_A):self.velocity_x -= self.SPEED * dt # type: ignore
        if pr.is_key_down(pr.KEY_S):self.velocity_y += self.SPEED * dt # type: ignore
        if pr.is_key_down(pr.KEY_W):self.velocity_y -= self.SPEED * dt # type: ignore
        
        self.velocity_x *= 0.8
        self.velocity_y *= 0.8
        
        self.x +=  self.velocity_x
        self.y +=  self.velocity_y
        
    def draw(self):
        pr.draw_circle(int(self.x), int(self.y), 20, pr.RED)