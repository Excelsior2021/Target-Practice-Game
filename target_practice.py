import pygame
from pygame.sprite import Group

from ship import Ship
from target import Target
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from button import Button
from heads_up_display import HUD
from miss_line import MissLine

def run_game(): 
    '''Initialise game and create screen'''
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_depth))
    pygame.display.set_caption('Target Practice')
    
    bullets_target = []
    ship = Ship(screen)
    bullets = Group()
    stats = GameStats(settings, bullets_target)
    target = Target(settings, screen, stats)
    play_button = Button(screen, 'Play')
    hud = HUD(screen, settings, stats, bullets_target)
    m_line = MissLine(settings, screen)

    while True:

        gf.check_events(settings, screen, stats, ship, target, bullets, play_button, hud)

        if stats.game_active:       
            ship.update_position(settings)
            gf.check_bullet_target_collisions(settings, stats, target, bullets, bullets_target, hud)
            gf.check_bullet_screen_edge_collision(stats, screen, target, bullets, hud)

        gf.update_screen(settings, screen, stats, ship, bullets, target, play_button, hud, m_line)

        #Checks

        #print(stats.bullets_left)
        #print(len(bullets))
        #print(len(bullets_target))
        #print(settings.target_speed)
        #print(settings.ship_speed)
        #print(target.height)
        #print(stats.stage)

run_game()   