from pygame.sprite import Group
from   pygame.time import Clock
import pygame, sys

from bird import Bird

pygame.init()

class Display(object):
    def __init__(self, title: str, size: tuple[int, int]):
        self.surface = pygame.display.set_mode(size);\
                       pygame.display.set_caption(title)

        self.clear  = self.surface.fill
        self.update = pygame.display.flip


class Game(object):

    def __init__(self) -> None:
        self.clock   = Clock()
        self.display = Display('Flappy Bird', (600, 600))
        self.running = 1

        self.all_sprites_group = Group()
        self.bird = Bird(self.all_sprites_group)

    def start(self):
        while self.running:
            self.display.clear('cyan')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = 0

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

            self.all_sprites_group.update(
                deltatime=(
                    self.clock.tick(60) / 1000
                )
            )

            self.all_sprites_group.draw(self.display.surface)
            self.display.update()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game=Game()
    game.start()
