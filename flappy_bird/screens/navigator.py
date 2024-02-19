from .abstract_screen import AbstractScreen

class Navigator(object):

    def __init__(self, initial: str, *screens: AbstractScreen) -> None:
        self.current = initial
        self.screens = { 
            screen.name: screen for screen in screens 
        }

    def execute(self):
        while True:
            self.screen      = self.screens[self.current]
            self.current     = self.screen.move
            self.screen.move = self.screen.name

            self.screen.update()
            self.screen.render()

