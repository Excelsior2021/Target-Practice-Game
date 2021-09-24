import pygame

class Ship():
    '''A model of a ship for sideway shooter'''
    def __init__(self, screen):
        self.screen = screen

        #Load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Load ship to screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        #Movement flag
        self.moving_up = False
        self.moving_down = False

    def update_position(self, settings):
        '''Updates ship's position based on movement flag'''
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += settings.ship_speed

    def blitme(self):
        '''Draw the ship at current location'''
        self.screen.blit(self.image, self.rect)

