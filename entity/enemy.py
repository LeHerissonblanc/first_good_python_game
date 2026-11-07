import pyray as pr
from entity.entity import Entity, State, Shape

class Enemy(Entity):
    def __init__(self, x, y, speed, color, target):
        super().__init__(
            x=x,
            y=y,
            size=pr.Vector2(35, 35),
            speed=speed,
            color=color,
            state=State.DYNAMIC,
            shape=Shape.CIRCLE
        )
        self.target = target

    def update(self, dt: float):
        target_position = self.target.position
        target_direction = self.target.direction

        direction_to_target = pr.Vector2(
            target_position.x - self.position.x,
            target_position.y - self.position.y,
        )

        if pr.vector2_length(direction_to_target) > 0:
            direction_to_target = pr.vector2_normalize(direction_to_target)

        self.velocity = pr.Vector2(
            direction_to_target.x * self.speed,
            direction_to_target.y * self.speed,
        )

        super().update(dt)
