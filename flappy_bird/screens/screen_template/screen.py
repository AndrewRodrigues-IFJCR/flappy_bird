from ..abstract_screen import AbstractScreen
from .settings import Settings

class Screen(AbstractScreen):
    settings: Settings

    def __init__(self, settings: Settings) -> None:
        super().__init__(settings)

    def update(self):
        ...

    def render(self):
        ...
