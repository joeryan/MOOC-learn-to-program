# File:                 : maze_tests.py
# Author:               : Joe Ryan <joe@clanryan.us>
# License:              : creative commons
# Description:          : tests Rat Maze Game, Learn to Code 2 - Assignment 2
# Arguments:            : none

require a2
require unittest

class TestMazeClass(unittest.TestCase):
    def setUp(self):
        
        maze = a2.Maze([['#', '#', '#', '#', '#', '#','#'],
                    ['#', '.', '.', '.', '.', '.', '#'],
                    ['#', '.', '#', '#', '#', '.', '#'],
                    ['#', '.', '.', '@', '#', '.', '#'],
                    ['#', '@', '#', '.', '@', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '#']],
                       a2.Rat('J', 1, 1),
                       a2.Rat('P', 1, 4))

