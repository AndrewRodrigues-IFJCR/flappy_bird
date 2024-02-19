from .widget import Widget
import pygame

class Label(Widget):

    def __init__(self,
            center_x: int,
            center_y: int,
            text : str,
            color: str,
            font_path: str, 
            font_size: int,
            antialias: bool = False
        ):
        super().__init__(center_x, center_y)
        self.text = text
        self.color = color
        self.font = pygame.font.Font(font_path, font_size)
        self.image = self.font.render(self.text, antialias, self.color)
