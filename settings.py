import pygame

class Settings:
    """A class to store all settings for Alien_invasion game"""

    def __init__(self):
        """Initialize the game settings"""
        #screen settings
        self.screen_width = 1366
        self.screen_height = 688
        self.space_bkg = pygame.image.load('images\space_bkg.png')
        self.space_bkg = pygame.transform.scale(self.space_bkg, (1366, 860))
   
        
        
        #Alien Settings
        self.alien_speed = 20
        self.fleet_drop_speed = 10
        #Fleet direction = 1 means right and -1 means left
        self.fleet_direction = 1
         #Missiles config
        self.missile_speed = 6.0
        self.missile_width = 2000
        self.missile_height = 25
        self.missile_color = (255,165,0)
        self.missile_limit = 10
        

        #sets the speed of the ship
        self.ship_speed = 8
        self.ship_limit = 1

        #alien speed scale
        self.speedup_scale = 1.1 
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """"settings for each phase"""
        self.ship_speed = 1.5
        self.alien_speed = 1.5
        self.missile_speed = 2.5
        # 1 means right and -1 left
        self.fleet_direction = 1   

    def increase_speed(self):
        """increase speed of the game"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.missile_speed *= self.speedup_scale

       



