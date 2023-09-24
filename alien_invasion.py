import sys
import pygame
from settings import Settings
from ship import Ship
from missiles import Missile
from alien import Alien

class AlienInvasion:
        """Overall class to manage game assets and behavior."""

        def __init__(self):
            """Initialize the game, and create game resources."""
            pygame.init()
            self.clock = pygame.time.Clock()
            self.settings = Settings()
            
            self.screen = pygame.display.set_mode(
                 (self.settings.screen_width, self.settings.screen_height))
            
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            
            
            pygame.display.set_caption("Alien Invasion")

            self.ship = Ship(self)
            self.missiles = pygame.sprite.Group()
            self.aliens = pygame.sprite.Group()
            self._create_fleet()

        def _create_fleet(self):
            """create a fleet of aliens"""
            #fill the screen with alien.
            #space between aliens
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size

            current_x, current_y = alien_width, alien_height
            while current_y < (self.settings.screen_height - (-2)   * alien_height):
                while current_x < (self.settings.screen_width - (-3) * alien_width):
                    self._create_alien(current_x,current_y)
                    current_x += 2 * alien_width

                # Finished a row; reset x value, and increment y value.
                current_x = alien_width
                current_y += 3 * alien_height

        def _create_alien(self, x_position, y_position):
            """add alien rows"""
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)
            




            
          
        
        def run_game(self):
            """Start the main loop for the game."""
            while True:
                self._check_events()
                self.ship.update()
                self.update_missile()
                self._update_screen()
                self.clock.tick(60)
                self.missiles.update()
            
                           
        def _check_events(self):
                """respond to keypresses and mouse events"""
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        self._check_keydown_events(event)
                    elif event.type == pygame.KEYUP:
                        self._check_keyup_events(event)
                        
        def _check_keydown_events(self, event):
                """"Keypress events"""
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_missile()
                    
        def _check_keyup_events(self, event):
                """Respond to key press"""
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

        def _fire_missile(self):
            """Creata a missile and add to the group"""
            if len(self.missiles) < self.settings.missile_limit:
                new_missile = Missile(self)
                self.missiles.add(new_missile)

        def update_missile(self):
            """Handle launched missiles and delete the old ones"""
            # Update missiles
            self.missiles.update()
    
            # Get rid of missiles that have disappeared by deleting old missiles
            for missile in self.missiles.copy():
                if missile.rect.bottom <= 0:
                    self.missiles.remove(missile)
        


        def _update_screen(self):
                """Update images on the screen and flip to the new screen"""
                self.screen.blit(self.settings.bkg_image, (0, 0))

                for missile in self.missiles.sprites():
                    missile.draw_missil()
                self.ship.blitme()
                self.aliens.draw(self.screen)
                
                pygame.display.flip()
              
if __name__ == '__main__':
    # Make a game instance, and run the game. or something else
    ai = AlienInvasion()
    ai.run_game()