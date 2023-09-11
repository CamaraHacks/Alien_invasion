class Settings:
    """A class to store all settings for Alien_invasion game"""

    def __init__(self):
        """Initialize the game settings"""
        #screen settings
        self.screen_width = 1366
        self.screen_height = 688
        self.bg_color = (41, 40, 50)
        
        #Missiles config
        self.missile_speed = 2.0
        self.missile_width = 3
        self.missile_height = 15
        self.missile_color = (60, 60, 60)
        

        #sets the speed of the ship
        self.ship_speed = 3