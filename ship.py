import pygame

class Ship:
    """A class to handle the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #Movent flag; start with a ship that is not moving
        self.moving_right = False
        self.moving_left = False

        #load the ship image and gets its rect.
        self.image = pygame.image.load('D:\Projects\Alien_invasion\images\green_ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom ceter of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ship exact horizontal pos
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        #update the x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect from self x
        self.rect.x = self.x

    def blitme(self):
        """Draw the shit at its current location"""
        self.screen.blit(self.image, self.rect) 