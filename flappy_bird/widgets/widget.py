from dataclasses import dataclass
from pygame.surface import Surface

@dataclass
class Widget:
    center_x: int
    center_y: int

    def update(self):...
    def render(self, screen: Surface):...
