class Settings:
    """A class to store all settings for Alien_invasion game"""

    def __init__(self):
        """Initialize the game settings"""
        #screen settings
        self.screen_width = 1366
        self.screen_height = 688
        self.bg_color = (41, 40, 50)

        #sets the speed of the ship
        self.ship_speed = 3