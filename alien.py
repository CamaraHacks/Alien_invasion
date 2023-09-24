import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien ships squadron"""

    def __init__(self, ai_game):
        """Initialize aliens starting pos"""
        super().__init__()
        self.screen = ai_game.screen

        #load alien image
        self.image = pygame.image.load('D:\Projects\Alien_invasion\images\ship_alien.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
