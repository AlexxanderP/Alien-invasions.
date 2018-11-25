class GameStats():
    """Track game stats"""

    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start game in inactive state
        self.game_active = False

        #Save the High Scores
        self.high_score = 0

    def reset_stats(self):
        """Initializes in game changing stats"""
        self.ships_left = self.ai_settings.ship_limit
        self.score  = 0
        self.level = 1
