import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien ships squadron"""

    def __init__(self, ai_game):
        """Initialize aliens starting pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load alien image
        self.image = pygame.image.load('images\ship_alien.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """aliens move to the other direction when hit the edge of the galaxy"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

   