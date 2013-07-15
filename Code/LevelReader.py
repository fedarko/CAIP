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
LevelReader.py
-----
class LevelReader: reads through a level and
creates cells, which are added to a sprite group
in SpriteManager.
"""

import Cell
import Levels
from Config import *

import pygame
from pygame.locals import *

class LevelReader(object):
    """Reads through a given level list and sets up the cells
    in the level."""
    
    def __init__(self, levelnum, sprite_manager):
        """Sets some attributes of the LevelReader."""
        
        self.levelnum = levelnum
        self.sprite_manager = sprite_manager
        
        # Dict relating topleft of cells to the cell.
        # Used in CellManager.
        self.topleftToCell = {}
        
    def read(self):
        """Reads through Levels.level1 and creates cells."""
        
        x = 0
        y = 0
        for string in Levels.level1:
            for char in string:
                if char == "#":
                    c = Cell.Cell((x, y), True)
                else:
                    c = Cell.Cell((x, y), False)
                self.sprite_manager.cells.add(c)
                self.topleftToCell[(x, y)] = c
                x += TILESIZE[0]
            y += TILESIZE[1]
            x = 0
