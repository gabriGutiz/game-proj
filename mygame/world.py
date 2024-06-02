import pygame
import random
import sys

from mygame.conf import SC_WIDTH, SC_HEIGHT, PLAYER_SIZE
from mygame._player import Player
from mygame._poo import Poo


class World:

    def __init__(self, screen, fps):
        self.screen = screen
        self.fps = fps

        self.player = pygame.sprite.GroupSingle()
        self.poos = pygame.sprite.Group()

        self.game_over = False
        self.player_score = 0
        self.game_level = 1

        self._add_points = 5

        self._right_border = SC_WIDTH - 40
        self._bottom_border = SC_HEIGHT - 60

        self._generate_world()


    def _generate_world(self):
        # create player
        player_x, player_y = 10 + PLAYER_SIZE // 2, SC_HEIGHT // 2
        center_size = PLAYER_SIZE // 2
        player_pos = (player_x, player_y - center_size)
        self.player.add(Player(player_pos, PLAYER_SIZE))


    def _player_move(self):
        # get key pressed and make movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and not self.game_over or keys[pygame.K_LEFT] and not self.game_over:
            if self.player.sprite.rect.left > 0:
                self.player.sprite.move_left()
        if keys[pygame.K_d] and not self.game_over or keys[pygame.K_RIGHT] and not self.game_over:
            if self.player.sprite.rect.right < self._right_border:
                self.player.sprite.move_right()
        if keys[pygame.K_w] and not self.game_over or keys[pygame.K_UP] and not self.game_over:
            if self.player.sprite.rect.top > 0:
                self.player.sprite.move_up()		
        if keys[pygame.K_s] and not self.game_over or keys[pygame.K_DOWN] and not self.game_over:
            if self.player.sprite.rect.bottom < SC_HEIGHT:
                self.player.sprite.move_bottom()

        # game restart button
        if keys[pygame.K_r]:
            self.game_over = False
            self.player_score = 0
            self.game_level = 1

            self._generate_world()


    def _detect_collisions(self):
        poo_to_player_collision = pygame.sprite.groupcollide(self.poos, self.player, True, False)
        if poo_to_player_collision:
            self.player.sprite.life -= 1


    def _update_poos(self):
        for poo in self.poos.sprites():
            if not poo.alive:
                continue

            result = poo.update_poo()
            if result:
                self.player_score += self._add_points


    def _add_poos(self):
        for _ in range(self.game_level*2):
            my_y = PLAYER_SIZE * random.randint(1, self._bottom_border)
            self.poos.add(Poo((self._right_border, my_y), PLAYER_SIZE, self.game_level))


    def _check_game_state(self):
        # check if game over
        if self.player.sprite.life <= 0:
            self.game_over = True
            sys.exit()
            # show game over message

        # check if next level
        if len(self.poos) == 0 and self.player.sprite.life > 0:
            self.game_level += 1


    def _update(self):
        self._player_move()

        self._detect_collisions()

        # rendering player and poos
        self._update_poos()
        self.poos.draw(self.screen)

        self.player.update()
        self.player.draw(self.screen)

        self._add_poos()

        self._check_game_state()

        pygame.display.update()

        print(f'Score: {self.player_score} | Life: {self.player.sprite.life} | Level: {self.game_level}')


    def run(self):

        while True:
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._update()
            self.fps.tick(30)

