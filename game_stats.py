class GameStats():
    '''Track stats for Target Practice'''
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        '''Rest game stats'''
        self.bullets_left = self.settings.bullet_misses