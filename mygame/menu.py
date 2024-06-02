import pygame
import sys

from mygame.conf import UPPER_NAME, SC_WIDTH
from mygame.actions import PLAY_ACTION, OPTS_ACTION
from mygame._button import Button
from mygame._constants import BK_GROUND, RECT, MENU_TITLE_COLOR
from mygame._utils import get_font

class Menu:

    def __init__(self, screen):
        self.screen = screen

        #self._background = pygame.image.load(BK_GROUND)
        self._x_center = int(SC_WIDTH / 2)
        self._btn_width, self._btn_height = (300, 80)
        self._btn_step = self._btn_height + 15
        self._first_btn_y = 160
        self._btn_font_size = 35


    def run(self):
        while True:
            #self.screen.blit(self._background, (0, 0))
            self.screen.fill("black")

            mouse_position = pygame.mouse.get_pos()

            menu_text = get_font(50).render(UPPER_NAME, True, MENU_TITLE_COLOR)
            menu_rect = menu_text.get_rect(center=(self._x_center, 60))

            btn_img = pygame.transform.scale(pygame.image.load(RECT),
                                             size=(self._btn_width, self._btn_height))

            play_bt = Button(image=btn_img, text_input="PLAY", hovering_color="White",
                             font=get_font(self._btn_font_size), base_color="#d7fcd4",
                             pos=(self._x_center, self._first_btn_y))
            opts_bt = Button(image=btn_img, text_input="OPTIONS", hovering_color="White",
                             font=get_font(self._btn_font_size), base_color="#d7fcd4",
                             pos=(self._x_center, self._first_btn_y + self._btn_step))
            quit_bt = Button(image=btn_img, text_input="QUIT", hovering_color="White",
                             font=get_font(self._btn_font_size), base_color="#d7fcd4",
                             pos=(self._x_center, self._first_btn_y + 2*self._btn_step))

            self.screen.blit(menu_text, menu_rect)

            for button in [play_bt, opts_bt, quit_bt]:
                button.change_color(mouse_position)
                button.update(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_bt.check_for_input(mouse_position):
                        return PLAY_ACTION
                    if opts_bt.check_for_input(mouse_position):
                        return OPTS_ACTION
                    if quit_bt.check_for_input(mouse_position):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

