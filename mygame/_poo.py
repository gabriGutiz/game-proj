import pygame

from mygame.conf import POO_SPEED
from mygame._constants import POO_PNG


class Poo(pygame.sprite.Sprite):

    def __init__(self, pos: tuple, size: int, level: int):
        super().__init__()
        self.x, self.y = pos

        self.image = pygame.image.load(POO_PNG)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.move_speed = POO_SPEED + level*5


    def _move(self):
        self.rect.x -= self.move_speed


    def update(self):
        self._move()
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))


    def update_poo(self) -> bool:
        self.update()

        if self.rect.left <= 0:
            self.kill()
            return True
        return False

