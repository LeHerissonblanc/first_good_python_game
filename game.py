import pyray as pr # type: ignore
from entity.entity import Entity
from entity.player import Player
from entity.entity import State

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.entities = []

        # player
        self.player = Player(
            x= screen_width / 2,
            y= screen_height / 2,
            height= 20,
            speed= 200,
            state= State.DYNAMIC,
        )
        self.entities.append(self.player)
        
        #others

    def update(self, dt: float):
        # Met à jour toutes les entités, joueur compris
        for entity in self.entities:
            entity.update(dt)

    def draw(self, bg_color):
        pr.begin_drawing()
        pr.clear_background(bg_color)

        for entity in self.entities:
            entity.draw()

        pr.end_drawing()
