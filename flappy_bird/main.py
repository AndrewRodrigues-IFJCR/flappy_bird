from screens import*
from settings import Settings
import pygame

pygame.init()
settings = Settings()
pygame.display.set_mode(
    (
        settings.width,
        settings.height
    )
)
pygame.display.set_caption(settings.title)
Navigator(settings.screen_initial,
    SCREEN_INITIAL,
    SCREEN_GAME,
    SCREEN_GAME_OVER
).execute()
