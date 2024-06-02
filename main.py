import pygame, sys

from mygame import Menu, World, Tutorial, Settings, conf, actions


def main():
    pygame.init()

    screen = pygame.display.set_mode((conf.SC_WIDTH, conf.SC_HEIGHT))
    pygame.display.set_caption(conf.NAME)
    fps = pygame.time.Clock()

    while True:
        menu = Menu(screen)
        action = menu.run()

        match action:
            case actions.PLAY_ACTION:
                world = World(screen, fps)
                world.run()
            case actions.TUTO_ACTION:
                tuto = Tutorial(screen)
                tuto.run()
            case actions.SETT_ACTION:
                sett = Settings(screen)
                sett.run()
            case _:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()

