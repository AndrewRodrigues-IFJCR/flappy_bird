from ..abstract_settings import AbstractSettings
from dataclasses import dataclass

@dataclass
class SettingsButton(AbstractSettings):
    move: str
    size_x: int
    size_y: int
    center_x: int
    center_y: int
    hover_color : str = 'blue'
    click_color : str = 'green'
    normal_color: str = 'red'

class Settings(AbstractSettings):
    button_start   : SettingsButton = SettingsButton('screen_game', 100, 50, 300, 500)
    button_credits : SettingsButton = SettingsButton('', 100, 50, 0, 0)
    button_settings: SettingsButton = SettingsButton('', 100, 50, 0, 0)
