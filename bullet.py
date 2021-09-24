import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A model of a bullet for Sideway Shooter'''
    def __init__(self, screen, ship):
        '''Create a bullet as ship's current position'''
        super().__init__()
        self.screen = screen
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = 60, 60, 60

        #Create bullet rect
        self.rect = pygame.Rect(0,0 , self.bullet_width, self.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

    def update_position(self):
        '''Move bullet across screen'''
        self.rect.x += 1
        self.rect.x = self.rect.x

    def draw_bullet(self):
        '''Draw bullet to the screen'''
        pygame.draw.rect(self.screen, self.bullet_colour, self.rect)


    