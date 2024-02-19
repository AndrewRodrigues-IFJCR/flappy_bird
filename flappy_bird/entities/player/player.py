from ..entity import Entity
from typing import Any
import pygame

class Player(Entity):

    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((100, 100))
        self.rect  = self.image.fill('red')
        self.rect.x = 300

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y += 1
        return super().update(*args, **kwargs)

    def jump(self):
        self.rect.y -= 50

