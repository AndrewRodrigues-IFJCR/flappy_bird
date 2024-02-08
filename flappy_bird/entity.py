from typing import Any, Dict, TypeAlias
from physics import REAL_SCALAR, PhysicsBody2D

import pygame
from pygame import Mask, Rect, Surface
from pygame.sprite import Sprite, AbstractGroup

Path: TypeAlias = str
Surf: TypeAlias = Surface
Body: TypeAlias = PhysicsBody2D

SurfProperty: TypeAlias = Surf | Path
RectProperty: TypeAlias = Surf | Rect
MaskProperty: TypeAlias = Surf | Mask
BodyProperty: TypeAlias = Body | Dict

get_surf = Surface
get_body = PhysicsBody2D

def get_imag(file: Path) -> Surface: return pygame.image.load(file).convert_alpha()
def get_rect(surf: Surface) -> Rect: return pygame.surface.Surface.get_rect(surf)
def get_mask(surf: Surface) -> Mask: return pygame.mask.from_surface(surf)

class Entity2D(Sprite):

    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
        self.surf = get_surf((50,  50))
        self.rect = get_rect(self.surf)
        self.mask = get_mask(self.surf)
        self.body = get_body()

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.body.update(kwargs.get('deltatime', REAL_SCALAR))
        self.image = pygame.transform.rotate(self.surf, self.body.angle)
        self.rect.centerx = int(self.body.position.x)
        self.rect.centery = int(self.body.position.y)
        return super().update(*args, **kwargs)

    @property
    def surf(self) -> Surface:
        """The surf property."""
        return self._surf

    @surf.setter
    def surf(self, surf: SurfProperty):
        if isinstance(surf, Surface):
            self._surf = surf
        else:
            self._surf = get_imag(surf)

    @property
    def rect(self) -> Rect:
        """The rect property."""
        return self._rect

    @rect.setter
    def rect(self, rect: RectProperty):
        if isinstance(rect, Rect):
            self._rect = rect
        else:
            self._rect = get_rect(rect)

    @property
    def mask(self) -> Mask:
        """The mask property."""
        return self._mask

    @mask.setter
    def mask(self, mask: MaskProperty):
        if isinstance(mask, Mask):
            self._mask = mask
        else:
            self._mask = get_mask(mask)

    @property
    def body(self) -> PhysicsBody2D:
        """The body property."""
        return self._body

    @body.setter
    def body(self, body: BodyProperty):
        if isinstance(body, PhysicsBody2D):
            self._body = body
        else:
            self._body = get_body(**body)

