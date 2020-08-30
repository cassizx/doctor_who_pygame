import sys
import pygame
import game_function as gf
from ship import Tardis
from settings import Settings
from background import Background

def start_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_heigth)
    )

    ship = Tardis(ai_settings , screen)

    background = Background(screen)

    pygame.display.set_caption('Doctor Who Game')

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, background)

start_game()