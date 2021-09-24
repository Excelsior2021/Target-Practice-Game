import pygame

class GameOver():
    '''Game over image'''
    def __init__(self, screen):
        self.screen = screen

        #Load image and get rect
        self.image = pygame.image.load('images/game_over.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Position image
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        '''Draw game over onto screen'''
        self.screen.blit(self.image, self.rect)