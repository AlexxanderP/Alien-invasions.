class GameStats():
    """Track game stats"""

    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True
        
    def reset_stats(self):
        """Initializes in game changing stats"""
        self.ships_left = self.ai_settings.ship_limit

