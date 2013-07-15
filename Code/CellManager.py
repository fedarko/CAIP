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
CellManager.py
-----
class CellManager: Switches cells on or off
based on the cells around them.
"""

import Levels
import Rule
import Cell
from Config import *

import time
import pygame
from pygame.locals import *

class CellManager(object):
    """Manages the cells by switching them on or
    off."""
    
    def __init__(self, cells, topleftToCell):
        """Sets the attributes of the CellManager."""
        
        self.cells = cells
        
        # The necessary changes to each cell are tracked in this dict
        # and then performed when each cell has been processed
        self.changes = {}
                
        self.topleftToCell = topleftToCell
        
        self.rule = Rule.Rule()
                
    def find_cell(self, pos):
        """Finds a cell with a topleft at pos and returns it.
        This uses self.topleftToCell, and as such is a lot faster
        than just searching through self.cells."""
        
        try:
            c = self.topleftToCell[pos]
        except KeyError:
            # There is no cell at the position
            return None
        return c
                
    def update_cells(self):
        """Reads through a level and calls various methods to
        either change or leave cells the same."""

        oncount = 0
        for c in self.cells:

            # The cells surrounding c are as follows:
            # 1 2 3
            # 4 c 5
            # 6 7 8
            # This is called c's Moore neighborhood
            c1p = (c.rect.left - TILESIZE[0], c.rect.top - TILESIZE[1])
            c2p = (c.rect.left, c.rect.top - TILESIZE[1])
            c3p = (c.rect.left + TILESIZE[0], c.rect.top - TILESIZE[1])
            c4p = (c.rect.left - TILESIZE[0], c.rect.top)
            c5p = (c.rect.left + TILESIZE[0], c.rect.top)
            c6p = (c.rect.left - TILESIZE[0], c.rect.top + TILESIZE[1])
            c7p = (c.rect.left, c.rect.top + TILESIZE[1])
            c8p = (c.rect.left + TILESIZE[0], c.rect.top + TILESIZE[1])

            for s in (c1p, c2p, c3p, c4p, c5p, c6p, c7p, c8p):
                if not self.find_cell(s):
                    continue
                if self.find_cell(s).on:
                    oncount += 1
            
            # Finally, handle the current cell
            result = self.rule.rule(oncount, c)
            if result == -1 or result == 1:
                self.changes[c] = result
            oncount = 0
        
        # Now all the cells have been processed
        for i in self.changes:
            if self.changes[i] == -1:
                i.switch_off()
            elif self.changes[i] == 1:
                i.switch_on()
        self.changes = {}
        
        time.sleep(GEN_WAIT)
