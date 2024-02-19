from __future__ import annotations
from ..abstract_screen import AbstractScreen
from .settings import Settings, SettingsButton
from widgets import ButtonWithColor
import pygame, sys

class NavButton(ButtonWithColor):

    def __init__(self, screen: Screen, settings: SettingsButton) -> None:
        self.screen = screen
        self.settings = settings
        super().__init__(
            settings.center_x,
            settings.center_y,
            settings.size_x,
            settings.size_y,
            settings.normal_color,
            settings.hover_color,
            settings.click_color
        )

    def on_click(self): super().on_click(); self.screen.move = self.settings.move

class Screen(AbstractScreen):
    settings: Settings

    def __init__(self, settings: Settings) -> None:
        super().__init__(settings)
        self.button_start    = NavButton(self, settings.button_start)
        self.button_credits  = NavButton(self, settings.button_credits)
        self.button_settings = NavButton(self, settings.button_settings)

        #
        self.group_buttons = pygame.sprite.Group()
        self.group_buttons.add(self.button_start)
        self.group_buttons.add(self.button_credits)
        self.group_buttons.add(self.button_settings)

        #
        self.button_select = [
            self.button_start,
            self.button_settings,
            self.button_credits
        ]
 
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.button_select[0], self.button_select[1], self.button_select[2] =\
                    self.button_select[1], self.button_select[2], self.button_select[0]

                if event.key == pygame.K_DOWN:
                    self.button_select[1], self.button_select[2], self.button_select[0] =\
                    self.button_select[0], self.button_select[1], self.button_select[2]

                button = self.button_select[0]
                if event.key == pygame.K_RETURN:
                    button.on_click()

                pygame.mouse.set_pos(
                    button.center
                )

        self.group_buttons.update()

    def render(self):
        surface = pygame.display.get_surface()
        self.group_buttons.draw(surface)
        pygame.display.flip()

