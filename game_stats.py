class Game_status:
    """track game score and stats"""
    
    def __init__(self, ai_game):
        """Initiliaze game components"""
        self.settings = ai_game.settings
        self.reset_status()
    
    def reset_status(self):
        """initialize game stats"""
        self.ship_left = self.settings.ship_limit