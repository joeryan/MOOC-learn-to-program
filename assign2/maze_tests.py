# File:                 : maze_tests.py
# Author:               : Joe Ryan <joe@clanryan.us>
# License:              : creative commons
# Description:          : tests Rat Maze Game, Learn to Code 2 - Assignment 2
# Arguments:            : none

import a2
import unittest

class TestMazeClass(unittest.TestCase):
    def setUp(self):
        jen = a2.Rat('J', 1, 1)
        paul = a2.Rat('P', 1, 4)
        maze = a2.Maze([['#', '#', '#', '#', '#', '#','#'],
                    ['#', '.', '.', '.', '.', '.', '#'],
                    ['#', '.', '#', '#', '#', '.', '#'],
                    ['#', '.', '.', '@', '#', '.', '#'],
                    ['#', '@', '#', '.', '@', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '#']],
                       jen, paul)

    # test initialization of rat
    def test_rat_J_symbol(self):
        assertEqual(jen.symbol, 'J')

    def test_rat_J_row(self):
        assertEqual(jen.row, 1)
        
    def test_rat_J_column(self):
        assertEqual(jen.col, 1)
    
    # test methods of rat
    def test_set_location(self):
        jen.set_location(1,2)
        assertEqual((jen.row, jen.col), (1, 2))

    def test_eat_sprout(self):
        jen.eat_sprout()
        assertEqual(jen.num_sprouts_eaten, 1)

    def test_string_representation__str(self):
        expected_str = "J at (1, 1) ate 0 sprouts."
        assertEqual(jen.__str__(), expected_str)

    # tests for initialization of maze
    def test_rat1_in_maze(self):
        assertEqual(maze.rat_1, jen)

    def test_rat2_in_maze(self):
        assertEqual(maze.rat_2, paul)
        
    # test methods of maze
    def test_is_wall_on_wall(self):
        assert maze.is_wall(0,0)

    def test_is_wall_not_on_wall(self):
        assert not(maze.is_wall(1,2))

    def test_get_character(self):
        assertEqual(maze.get_character(3,4), '@')

    def test_move_a_rat_into_hall(self):
        assert maze.move(jen, NO_CHANGE, RIGHT)

    def test_move_rat_into_wall(self):
        assert not(maze.move(paul, DOWN, NO_CHANGE))

    def test_string_representation__str__(self):
        expected_str = ("#######\n#J..P.#\n#.###.#\n#..@#.#\n#@#.@.#\n#######\n" +
                        "J at (1, 1) ate 0 sprouts.\n" +
                        "P at (1, 4) ate 0 sprouts.")
        assertEqual(maze.__str__(), expected_str)

    
                                     
                                     
                    
if __name__ == '__main__':
    unittest.main()
