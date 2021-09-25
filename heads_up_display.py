import pygame.font

class HUD():
    '''A class that shows game information'''
    def __init__(self, screen, settings, stats, bullets_target):
        '''Initialise HUD information'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.bullets_target = bullets_target

        #Font settings
        self.text_colour = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 32)

        self.prep_hits()

    def prep_hits(self):
        '''Prepare image for hits in game'''
        hits_str = 'Hits: ' + str(len(self.bullets_target))
        self.hits_image = self.font.render(hits_str, True, self.text_colour, 
            self.settings.bg_colour)

        #Display hits on screen
        self.hits_rect = self.hits_image.get_rect()
        self.hits_rect.left = self.screen_rect.left + 5
        self.hits_rect.top = self.screen_rect.top + 5

    def show_info(self):
        '''Draw info to screen'''
        self.screen.blit(self.hits_image, self.hits_rect)




