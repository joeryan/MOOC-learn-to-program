# File:                 : maze_tests.py
# Author:               : Joe Ryan <joe@clanryan.us>
# License:              : creative commons
# Description:          : tests Rat Maze Game, Learn to Code 2 - Assignment 2
# Arguments:            : none

import a2
import unittest

class TestMazeClass(unittest.TestCase):
    def setUp(self):
        self.jen = a2.Rat(a2.RAT_1_CHAR, 1, 1)
        self.paul = a2.Rat(a2.RAT_2_CHAR, 1, 4)
        self.maze = a2.Maze([['#', '#', '#', '#', '#', '#','#'],
                    ['#', '.', '.', '.', '.', '.', '#'],
                    ['#', '.', '#', '#', '#', '.', '#'],
                    ['#', '.', '.', '@', '#', '.', '#'],
                    ['#', '@', '#', '.', '@', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '#']],
                       self.jen, self.paul)

    # test initialization of rat
    def test_rat_J_symbol(self):
        # self.jen = a2.Rat(a2.RAT_1_CHAR, 1,2)
        self.assertEqual(self.jen.symbol, 'J')

    def test_rat_J_row(self):
        self.assertEqual(self.jen.row, 1)
        
    def test_rat_J_column(self):
        self.assertEqual(self.jen.col, 1)
    
    # test methods of rat
    def test_set_location(self):
        self.jen.set_location(1,2)
        self.assertEqual((self.jen.row, self.jen.col), (1, 2))

    def test_eat_sprout(self):
        self.jen.eat_sprout()
        self.assertEqual(self.jen.num_sprouts_eaten, 1)

    def test_string_representation__str(self):
        expected_str = "J at (1, 1) ate 0 sprouts."
        self.assertEqual(self.jen.__str__(), expected_str)

    # tests for initialization of maze
    def test_rat1_in_maze(self):
        self.assertEqual(self.maze.rat_1, self.jen)

    def test_rat2_in_maze(self):
        self.assertEqual(self.maze.rat_2, self.paul)
        
    # test methods of maze
    def test_is_wall_on_wall(self):
        assert self.maze.is_wall(0,0)

    def test_is_wall_not_on_wall(self):
        assert not(self.maze.is_wall(1,2))

    def test_get_character(self):
        self.assertEqual(self.maze.get_character(3,3), a2.SPROUT)

    def test_move_a_rat_into_hall(self):
        assert self.maze.move(self.jen, a2.NO_CHANGE, a2.RIGHT)

    def test_move_rat_into_wall(self):
        assert not(self.maze.move(self.paul, a2.DOWN, a2.NO_CHANGE))

    def test_string_representation__str__(self):
        expected_str = ("#######\n#J..P.#\n#.###.#\n#..@#.#\n#@#.@.#\n#######\n" +
                        "J at (1, 1) ate 0 sprouts.\n" +
                        "P at (1, 4) ate 0 sprouts.")
        self.assertEqual(self.maze.__str__(), expected_str)

    
                                     
                                     
                    
if __name__ == '__main__':
    unittest.main()
