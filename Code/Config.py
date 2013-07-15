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
Config.py
-----
This file contains some variables that change the game.
"""

#### Vital ####
# RULESTRING /str / "survival count/birth count" : Defines
# the rule for the life-like cellular automaton. The first
# part of the string is how many cells must be on around a
# cell for that cell to survive, and the second part is how
# many cells must be on around an off cell for that cell to
# be born.
# You can find tons of rulestrings on the internet. Some common
# ones are:
#
# -Conway's Game of Life: "23/3"
# -Maze: "12345/3"

RULESTRING = "23/3" # Default: "23/3"

#### Cells ####
# ONCOLOR /(R, G, B) : The color for an "on" cell.
#
# OFFCOLOR /(R, G, B) : The color for an "off" cell.
#
# TILESIZE /(int, int) : The size of a tile in the game.

ONCOLOR = (0, 0, 0) # Default: (0, 0, 0)

OFFCOLOR = (255, 255, 255) # Default: (255, 255, 255)

TILESIZE = (10, 10) # Default: (10, 10)

#### Background ####
# BGCOLOR /(R, G, B) : The color of the background, in an RGB triplet

BGCOLOR = (255, 255, 255) # Default: (255, 255, 255)

#### Display ####
# SCREENSIZE /(x, y) : The size of the window for the game, in pixels
#
# USE_FULLSCREEN /Bool : Whether or not to use fullscreen
#
# WINDOW_TITLE /str : The title of the game's window.

SCREENSIZE = (800, 600) # Default: (800, 600)

USE_FULLSCREEN = False # Default: False

WINDOW_TITLE = "Cellular Automata: Rule %s" % (RULESTRING) # Default: "Cellular Automata: Rule %s" % (RULESTRING)

#### Miscellaneous ####
# FPS /int : The frames per second at which the game runs
#
# GEN_WAIT /int : The time delay between each generation, in seconds.

FPS = 60 # Default: 60

GEN_WAIT = 0 # Default: 0
