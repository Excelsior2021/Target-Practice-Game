class GameStats():
    '''Track stats for Target Practice'''
    def __init__(self, settings, target, bullets_target):
        self.settings = settings
        self.target = target
        self.bullets_target = bullets_target
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        '''Rest game stats'''
        self.bullets_left = self.settings.target_misses_allowed
        self.bullets_target.clear()
