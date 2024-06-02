import pygame

from mygame._constants import PLAYER_PNG
from mygame.conf import PLAYER_SPEED


class Player(pygame.sprite.Sprite):

    def __init__(self, pos: tuple, size):
        super().__init__()
        self.x, self.y = pos

        self.image = pygame.image.load(PLAYER_PNG)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.player_speed = PLAYER_SPEED

        # player status
        self.life = 3


    def move_left(self):
        self.rect.x -= self.player_speed


    def move_up(self):
        self.rect.y -= self.player_speed


    def move_right(self):
        self.rect.x += self.player_speed


    def move_bottom(self):
        self.rect.y += self.player_speed


    def update(self):
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

