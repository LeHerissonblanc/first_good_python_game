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
        speed: int,
        state: State = State.DYNAMIC,
    ):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.height = height
        self.state = state
        self.SPEED = speed

    def update(self, dt: float):
        match self.state:
            case State.STATIC:
                pass
            case State.DYNAMIC:
                pass