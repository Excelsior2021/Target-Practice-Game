import pygame

class Target():
    '''A target to aim for in Sideway Shooter'''
    def __init__(self, settings, screen):
        '''Initialise target onto screen'''
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        self.target_width = 10
        self.target_height = 100
        self.target_colour = (255, 0, 0)

        #Create target rect and set position
        self.rect = pygame.Rect(0,0 , self.target_width, self.target_height)
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        self.centery = float(self.rect.centery)

    def update_target(self):
        self.centery -= (self.settings.target_speed*
                            self.settings.target_direction)
                            
        self.rect.centery = self.centery

    def check_edges(self):
        if self.rect.top == self.screen_rect.top:
            return True
        if self.rect.bottom == self.screen_rect.bottom:
            return True

    def draw_target(self):
        '''Draw target to the screen'''
        pygame.draw.rect(self.screen, self.target_colour, self.rect)
