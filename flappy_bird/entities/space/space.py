from pygame.surface import Surface
from ..entity import Entity

class Space(Entity):

    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.image = Surface((600, 600))
        self.rect  = self.image.fill('black')
        self.rect.center = (0,0)

