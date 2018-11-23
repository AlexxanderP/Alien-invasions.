class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed_factor = 1.89

        # Bullet settings.
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        
        #Fleet direction change(+1 = right, -1 = left)
        self.fleet_direction = 1

