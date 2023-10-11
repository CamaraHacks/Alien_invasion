import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from missiles import Missile
from alien import Alien
from game_stats import Game_status
from button import Button

class AlienInvasion:
        """Overall class to manage game assets and behavior.""" 
        def __init__(self):
            """Initialize the game, and create game resources."""
            pygame.init()   
            self.clock = pygame.time.Clock()
            self.settings = Settings()
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            pygame.display.set_caption("Alien Invasion")

            
            self.play_button = Button(self, "Play")

        #Create instance to store game statics
            self.status = Game_status(self)
            self.ship = Ship(self)
            self.missiles = pygame.sprite.Group()
            self.aliens = pygame.sprite.Group()
            self._create_fleet()

            self.game_active = False
            self._update_screen()
            

        def _ship_hit(self):
            """Ships explodes if being touched by aliens"""
            if self.status.ship_left > 0:
                #Decrement ships left
                self.status.ship_left -= 1
                #get rid of aliens and bullets
                self.missiles.empty()
                self.aliens.empty()
                #create new fleet and center the ship 
                self._create_fleet()
                self.ship.center_ship()
                sleep(0.6)
            else:
                self.game_active = False
                pygame.mouse.set_visible(False)
        

        def _check_aliens_bottom(self):
            """Check if any aliens have reached the bottom of the screen"""
            for alien in self.aliens.sprites():
                if alien.rect.bottom >= self.settings.screen_height:
                    self._ship_hit()
                    break

        def _create_fleet(self):
            """create a fleet of aliens"""
            #fill the screen with alien.
            #space between aliens
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size

            current_x, current_y = alien_width, alien_height
            while current_y < (self.settings.screen_height - (10)   * alien_height):
                while current_x < (self.settings.screen_width - (11) * alien_width):
                    self._create_alien(current_x,current_y)
                    current_x += 2 * alien_width

                # Finished a row; reset x value, and increment y value.
                current_x = alien_width
                current_y +=  2 * alien_height

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
                if self.game_active:
                    self.ship.update()
                    self.update_missile()
                    self._update_screen()
                    self.clock.tick(60)
                    self.missiles.update()
                    self._update_aliens()
                
                           
        def _check_events(self):
                """respond to keypresses and mouse events"""
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        self._check_keydown_events(event)
                    elif event.type == pygame.KEYUP:
                        self._check_keyup_events(event)

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        self._check_play_button(mouse_pos)   
        
        def _check_play_button(self, mouse_pos):
             """start the game after click on play button"""
             button_clicked =self.play_button.rect.collidepoint(mouse_pos)
             if button_clicked and not self.game_active:
                self.settings.initialize_dynamic_settings()
                self.status.reset_status()
                self.game_active = True       
            
            #Clear missiles and aliens
                self.missiles.empty()
                self.aliens.empty()

            #Create a new fleet and align the ship
                self._create_fleet()
                self.ship.center_ship()
                #hide mouse
                pygame.mouse.set_visible(False)
        
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
            #check if any bullets that have hit the aliens
            #if the bullets hit the aliens, explode the alien
            collision = pygame.sprite.groupcollide(
                self.missiles, self.aliens, True, True)
            if not self.aliens:
                self._create_fleet()
                self.missiles.empty()
                self.settings.increase_speed()
                sleep(0.5)
            

        def _update_screen(self):
                """Update images on the screen and flip to the new screen"""
                self.screen.blit(self.settings.space_bkg, (0, 0))
                for missile in self.missiles.sprites():
                    missile.draw_missil()
                self.ship.blitme()
                self.aliens.draw(self.screen)
                if not self.game_active:
                    self.play_button.draw_button()
                pygame.display.flip()

        def _update_aliens(self):
            """Check if the fleet is at an edge, then update positions."""
            self._check_fleet_edges()
            self.aliens.update() 
            self._check_aliens_bottom()

        #look for aliens collisions
            if pygame.sprite.spritecollideany( self.ship, self.aliens):
                self._ship_hit()
                

        def _check_fleet_edges(self):
             """responds if a alien reachs a edge"""
             for alien in self.aliens.sprites():
                  if alien.check_edges():
                        self._change_fleet_direction()
                        break
        
        def _change_fleet_direction(self):
            """Drop the entire fleet and change its direction."""
            for alien in self.aliens.sprites():
                alien.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1
  
        
if __name__ == '__main__':
    # Make a game instance, and run the game. or something else
    ai = AlienInvasion()
    ai.run_game()