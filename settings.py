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
        self.target_width = 10
        self.target_height = 100
        self.target_direction = 1

        #Miss line settings
        self.miss_line_width = 5
        self.miss_line_height = self.screen_depth

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        '''Initialise dynamic game settings'''
        #Ship settings
        self.ship_speed = 0.5

        #Target settings
        self.target_speed = 0.1

