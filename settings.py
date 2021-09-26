import pygame

class Settings():
    '''Sideway Shooter settings'''
    def __init__(self):
        '''Initialise static game settings'''
        #Screen settings
        self.screen_width = 600
        self.screen_depth = 600
        self.bg_colour = (230, 230, 230)

        #Bullet settings
        self.target_misses_allowed = 10

        #Target settings
        self.target_direction = 1

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        '''Initialise dynamic game settings'''
        #Ship settings
        self.ship_speed = 0.5

        #Target settings
        self.target_speed = 0.1
        
    def increase_speed(self):
        self.target_speed += 0.1
        self.ship_speed *= 1.1

