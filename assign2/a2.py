# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    def __init__(self, sym, row, col):
        """ (Rat, str, int, int) -> NoneType

        Initializes Rat instance with single char symbol, an int row,
        and an int column.
        """
        self.symbol = sym
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Set the rat's current location to the int row and int column provided.
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) -> NoneType

        increase num_sprouts_eaten by one.
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        Provide a string representation of the rat, it's position and number of
        sprouts eaten so far.
        """
        return ("%s at (%d, %d) ate %d sprouts." % (self.symbol,
                                                    self.row,
                                                    self.column,
                                                    self.num_sprouts_eaten))


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat, int) -> NoneType

        Initialize a Maze with the walls, halls, sprouts in maze (list
        of list of strings). the two rats in the maze, and a number of
        sprouts remaining.
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        # self.num_sprouts_left = num_sprouts_left

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        returns True if and only if there is a wall at the given row and column
        """
        return self[row[col]] == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        returns the character at the given row and column position in the maze.
        """
        if (self.rat_1.row, self.rat_1.col) == (row, col):
            return self.rat_1.symbol
        elif (self.rat_2.row, self.rat_2.col) == (row, col):
            return self.rat_2.symbol
        else:                                      
            return self.maze[row][col]

    def move(self, rat, vertical, horizontal):
        """ (Maze, Rat, int, int) -> bool

        move rat, eat brussel sprout if needed and make a hall, return True
        if and only if a wall wasn't in the way.
        """
        # determine new location
        new_row = rat.row + vertical
        new_col = rat.col + horizontal
        
        # check to see if move places rat on a wall and return False if it does
        if self.is_wall(new_row, new_col):
            return False
        
        # check to see if new location has a sprout, have rat eat it, adjust
        # number of sprouts left in the maze
        if self.get_character(new_row, new_col) == SPROUT:
            rat.eat_sprout()
            self.maze[new_row][new_col] = HALL
            self.num_sprouts_left -= 1

        # set rat's row and col to new location and return True
        rat.row = new_row
        rat.col = new_col
        return True

    def __str__(self):
        """ (Maze) -> str

        return a string representation of the maze for display
        """
        result = ""
        for i in range(len(self.maze)):
            for column in self.maze[i]:
                result += column
            result += "\n"

        result += self.rat_1.__str__() + "\n"
        result += self.rat_2.__str__()
        
    
