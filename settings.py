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
        self.alien_speed = 1

        #Missiles config
        self.missile_speed = 6.0
        self.missile_width = 5
        self.missile_height = 25
        self.missile_color = (255,165,0)
        self.missile_limit = 10
        

        #sets the speed of the ship
        self.ship_speed = 8

        #Alien Settings


