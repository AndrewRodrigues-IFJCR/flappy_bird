from .widget import Widget, dataclass
import pygame, enum

class States(enum.Enum):
    NORMAL = enum.auto()
    HOVER  = enum.auto()
    CLICK  = enum.auto()

@dataclass
class Button(Widget):
    size_x: int
    size_y: int
    

    def __post_init__(self):
        self.rect = pygame.Rect(
            self.center_x - self.size_x // 2,
            self.center_y - self.size_y // 2,
            self.size_x, 
            self.size_y
        )
    
    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse[0], mouse[1]):
            self.on_hover()
            if click:
                self.on_click()

        else: self.on_normal()

    def render(self, screen: Surface):
        pygame.draw.rect(screen, self.)

    def on_normal(self): self.state = States.NORMAL
    def on_hover (self): self.state = States.HOVER
    def on_click (self): self.state = States.CLICK



