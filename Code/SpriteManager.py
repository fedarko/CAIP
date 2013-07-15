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
SpriteManager.py
-----
class SpriteManager: Creates, draws, and updates
the cells in the game.
"""

import CellManager
import LevelReader
from Config import *

import pygame
from pygame.locals import *

class SpriteManager(object):
    """Manages the sprites in the game."""
    
    def __init__(self, screen):
        """Sets the attributes of the SpriteManager."""
        
        self.screen = screen        
        self.bg = pygame.Surface(SCREENSIZE)
        
        self.cells = pygame.sprite.RenderPlain()        
        lr = LevelReader.LevelReader(1, self)        
        self.cellManager = CellManager.CellManager(self.cells, lr.topleftToCell)
        
        lr.read()
    
    def update_sprites(self):
        """Updates the sprites, draws them to the screen,
        and then updates the display."""

        self.bg.fill(BGCOLOR)
        
        self.cellManager.update_cells()
        
        self.cells.draw(self.bg)
        
        self.screen.blit(self.bg, (0, 0))
        pygame.display.flip()
