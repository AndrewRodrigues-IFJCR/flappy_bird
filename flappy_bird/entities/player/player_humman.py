from .player import Player
import pygame

class PlayerHumman(Player):

    def update(self) -> None:
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.jump()
        return super().update()
