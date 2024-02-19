from abc import ABC, abstractmethod
from .abstract_settings import AbstractSettings
from inspect import getfile
from pathlib import Path

class AbstractScreen(ABC):
    name: str
    move: str

    def __init__(self, settings: AbstractSettings) -> None:
        self.settings = settings 
        module = Path(getfile(self.__class__))
        self.name = module.parent.name
        self.move = module.parent.name
        print(self.name)

    @abstractmethod
    def update(self): raise NotImplementedError

    @abstractmethod
    def render(self): raise NotImplementedError
