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
Rule.py
-----
class Rule: Decides what happens to a cell in the game.
"""

from Config import RULESTRING

class Rule(object):
    """A class that decides what happens to cells in the
    game."""

    def __init__(self):
        """Sets the attributes of class Rule."""
        
        self.s, self.b = self.process_rulestring(RULESTRING)

    def rule(self, oncount, cell):
        """Uses the survival and birth counts from the
        rulestring to decides what happens to a cell with
        a certain number of on cells in its Moore Neighborhood."""
                     
        if (oncount < min(self.s) or oncount > max(self.s)) and cell.on:
            # Death
            return -1
        if oncount in self.s and cell.on:
            # Cell stays the same
            return 0
        if oncount in self.b and cell.off:
            # Birth
            return 1

    def process_rulestring(self, rs):
        """Processes rs as a rulestring for life-like CA and
        returns a tuple containing the lists of oncounts for
        survival and birth."""
        
        s = []
        b = []
        r = rs.split("/")
        for i in r[0]:
            s.append(int(i))
        for i in r[1]:
            b.append(int(i))
        return s, b
