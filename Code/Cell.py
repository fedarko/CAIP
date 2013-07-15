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
Cell.py
-----
class Cell: Sprite class for a cell in the game.
"""

from Config import *

import os
import pygame
from pygame.locals import *

class Cell(pygame.sprite.Sprite):
    """A cell in the game of life."""
    
    def __init__(self, pos, on):
        """Sets the attributes of the cell."""
        
        super(Cell, self).__init__()
        
        self.image = pygame.Surface(TILESIZE)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
        if on:
            self.switch_on()
        else:
            self.switch_off()
    
    def switch_on(self):
        """Switches the cell on."""
        
        self.image.fill(ONCOLOR)
        self.on = True
        self.off = False
    
    def switch_off(self):
        """Switches the cell off."""
        
        self.image.fill(OFFCOLOR)
        self.off = True
        self.on = False
