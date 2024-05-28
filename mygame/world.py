import pygame
import sys


class World:

    def __init__(self, screen, fps):
        self.screen = screen
        self.fps = fps


    def _player_move(self):
        ...


    def _update(self):
        ...


    def run(self):

        while True:
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._player_move()
            self._update()
            pygame.display.update()
            self.fps.tick(30)

