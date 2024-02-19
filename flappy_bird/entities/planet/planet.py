import pygame
from pygame.surface import Surface
from ..enemy import Enemy

class Planet(Enemy):

    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.image = Surface((100, 100))
        self.rect  = self.image.fill((0,0,0,0))
        self.rect.center = (300, 300)
        pygame.draw.circle(self.image, (255,0,0), (50, 50), 50)
 
