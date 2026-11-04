import pyray as pr
from enum import Enum

class State(Enum):
    STATIC = "static"
    DYNAMIC = "dynamic"

class Entity:
    def __init__(
        self,
        x: float,
        y: float,
        height: int,
        speed: float,
        state: State = State.STATIC,
    ):
        self.position = pr.Vector2(x, y)
        self.velocity = pr.Vector2(0, 0)
        self.height = height
        self.speed = speed
        self.state = state
        
        if not isinstance(state, State):
            raise TypeError(f"state must be in enum State, received : {state!r}")

    def update(self, dt: float):
        if self.state == State.DYNAMIC:
            self.position.x += self.velocity.x * dt
            self.position.y += self.velocity.y * dt

