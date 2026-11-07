import pyray as pr
from entity.entity import Entity, State, Shape

class Player(Entity):
    def __init__(
        self, 
        x: float, 
        y: float, 
        speed: float,
        color: pr.Color,
        size = pr.Vector2(35,35)
    ):
        super().__init__(
            x= x,
            y= y,
            size= size,
            speed= speed,
            color= color,
            state= State.DYNAMIC,
            shape= Shape.CIRCLE
        )
        self.direction = pr.Vector2(0, 0)

    def update(self, dt: float):
        direction = pr.Vector2(0, 0)
        self.temp_speed = self.speed
                                                                        # because KEYS are missreceived by the wrapper
        if pr.is_key_down(pr.KEY_D): direction.x += 1                   # type: ignore
        if pr.is_key_down(pr.KEY_A): direction.x -= 1                   # type: ignore
        if pr.is_key_down(pr.KEY_S): direction.y += 1                   # type: ignore
        if pr.is_key_down(pr.KEY_W): direction.y -= 1                   # type: ignore
        if pr.is_key_down(pr.KEY_LEFT_SHIFT): self.temp_speed *= 1.5    # type: ignore

        if pr.vector2_length(direction) > 0:
            direction = pr.vector2_normalize(direction)

        self.direction = direction

        self.velocity = pr.Vector2(
            direction.x * self.temp_speed,
            direction.y * self.temp_speed,
        )

        super().update(dt)
