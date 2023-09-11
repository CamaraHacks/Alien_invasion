import pygame
from pygame.sprite import sprite

class Missile(sprite):
    """A class to handle missiles *o* """

    def __init__(self, ai_game):
        """Create a missiles obj at current ship pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.missile_color


    # Create a missil rect at (0, 0) and then set correct position.
    self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
    self.rect.midtop = ai_game.ship.rect.midtop

    #Store the missil pos
    self.y = float(self.rect.y)

    def update(self):
        """Move the missil up"""
        #Update the exact pos of the missiles
        self.y -= self.settings.bullet_speed
        #Update the rect pos
        self.rect.y =  self.y

    def draw_missil(self):
        """Draw the missile to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    