import pygame
from pygame.sprite import Group

from ship import Ship
from target import Target
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from button import Button

bullets_target = []

def run_game():
    '''Initialise game and create screen'''
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_depth))
    pygame.display.set_caption('Target Practice')
    
    ship = Ship(screen)
    bullets = Group()
    target = Target(settings, screen)
    stats = GameStats(settings)
    play_button = Button(screen, 'Play')

    while True:

        gf.check_events(settings, stats, ship, screen, bullets, play_button, bullets_target)
        if stats.game_active:       
            ship.update_position(settings)
            gf.check_bullet_target_collisions(settings, stats, screen, target, bullets, bullets_target)
        gf.update_screen(settings, screen, stats, ship, bullets, target, play_button)

        #Checks

        #print(stats.bullets_left)
        #print(len(bullets))
        #print(len(bullets_target))
        #print(settings.target_speed)
        #print(settings.ship_speed)

run_game()   