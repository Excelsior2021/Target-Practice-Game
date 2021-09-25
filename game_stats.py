class GameStats():
    '''Track stats for Target Practice'''
    def __init__(self, settings, bullets_target):
        self.settings = settings
        self.bullets_target = bullets_target
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        '''Rest game stats'''
        self.bullets_left = self.settings.target_misses
        self.bullets_target.clear()
