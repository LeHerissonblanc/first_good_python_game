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
                    pr.draw_circle(
                        int(self.position.x),
                        int(self.position.y),
                        self.size.x / 2,
                        self.color
                    )
                else:
                    raise TypeError("size x and size y must be equal for the circles")
            case Shape.RECT:
                pr.draw_rectangle(
                    int(self.position.x),
                    int(self.position.y),
                    int(self.size.x),
                    int(self.size.y),
                    self.color
                )
            case _:
                raise TypeError(f'{self} has no shape')