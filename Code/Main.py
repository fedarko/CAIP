"""
Copyright 2011 Marcus Fedarko
Contact Email: marcus.fedarko@gmail.com

This file is part of CAIP.

    CAIP is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CAIP is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CAIP.  If not, see <http://www.gnu.org/licenses/>.

====
Main.py
-----
class Main: Sets up pygame and runs the game's mainloop.
"""

import SpriteManager
from Config import *

import pygame
from pygame.locals import *

class Main(object):
    """The class that starts the game and runs the game's mainloop."""
    
    def __init__(self):
        """Sets up various aspects of pygame and calls the mainloop."""
        
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        
        if USE_FULLSCREEN:
            self.screen = pygame.display.set_mode(SCREENSIZE, FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(SCREENSIZE)
            
        self.sprite_manager = SpriteManager.SpriteManager(self.screen)        
        self.mainloop()
        
    def mainloop(self):
        """Manages the game's processes and checks
        for player input."""
        
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            
            for e in pygame.event.get():

                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    running = False
                        
            self.sprite_manager.update_sprites()
