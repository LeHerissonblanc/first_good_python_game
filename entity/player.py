import pyray as pr
from entity.entity import Entity, State


class Player(Entity):
    def __init__(self, x: float, y: float, height: int, speed: float):
        super().__init__(
            x=x,
            y=y,
            height=height,
            speed=speed,
            state=State.DYNAMIC,
        )

    def update(self, dt: float):
        direction = pr.Vector2(0, 0)

        if pr.is_key_down(pr.KEY_D): direction.x += 1 # type: ignore
        if pr.is_key_down(pr.KEY_A): direction.x -= 1 # type: ignore
        if pr.is_key_down(pr.KEY_S): direction.y += 1 # type: ignore
        if pr.is_key_down(pr.KEY_W): direction.y -= 1 # type: ignore

        if pr.vector2_length(direction) > 0:
            direction = pr.vector2_normalize(direction)

        self.velocity = pr.Vector2(
            direction.x * self.speed,
            direction.y * self.speed,
        )

        super().update(dt)

    def draw(self):
        pr.draw_circle(
            int(self.position.x),
            int(self.position.y),
            self.height,
            pr.RED,
        )
