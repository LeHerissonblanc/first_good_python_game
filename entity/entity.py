import pyray as pr
from enum import Enum

class State(Enum):
    STATIC = "static"
    DYNAMIC = "dynamic"

class Shape(Enum):
    CIRCLE = "circle"
    RECT = "rect"

class Entity:
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        size = pr.Vector2(10,10),
        speed: float = 0,
        color: pr.Color = pr.RED,
        state: State = State.STATIC,
        shape: Shape = Shape.RECT
    ):
        self.position = pr.Vector2(x, y)
        self.velocity = pr.Vector2(0, 0)
        self.size = size
        self.speed = speed
        self.state = state
        self.shape = shape
        self.color = color
        
        if not isinstance(state, State):
            raise TypeError(f"state must be in enum State, received : {state!r}")
        if not isinstance(shape, Shape):
            raise TypeError(f"shape must be in enum Shape, received : {shape!r}")

    def update(self, dt: float):
        if self.state == State.DYNAMIC:
            self.position.x += self.velocity.x * dt
            self.position.y += self.velocity.y * dt
    
    def draw(self):
        match self.shape:
            case Shape.CIRCLE:
                if self.size.x == self.size.y:
                    radius = self.size.x / 2

                    pr.draw_circle(
                        int(self.position.x),
                        int(self.position.y),
                        radius,
                        self.color,
                    )
                    pr.draw_circle_lines_ex(
                        self.position,
                        radius,
                        3,
                        pr.BLACK,
                    )
                else:
                    raise TypeError("size x and size y must be equal for the circles")
            case Shape.RECT:
                rect = pr.Rectangle(
                    self.position.x,
                    self.position.y,
                    self.size.x,
                    self.size.y,
                )
                pr.draw_rectangle_rec(rect, self.color)
                pr.draw_rectangle_lines_ex(rect, 3, pr.BLACK)
            case _:
                raise TypeError(f'{self} has no shape')