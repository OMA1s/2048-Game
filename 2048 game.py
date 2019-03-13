"""
Clone of 2048 game.
"""
import random
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
#Helper Functions
def list_creator(row, col, direction):
    '''
    creates initial list of row or col
    to traverse for
    '''
    templ = []
    if direction == 1:
        for num in range(0, col):
            templ.append((0,num))
        return templ
    elif direction == 2:
        row -=1
        col-= 1
        while col >-1:
            templ.append((row,col))
            col -= 1
        return templ
    elif direction == 3:
        for num in range(0, row):
            templ.append((num,0))
        return templ
    else:
        for num in range(0, row):
            templ.append((num,col-1))
        return templ
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    result = list(line)
    return slide_left(add_pairs(slide_left(result)))

def slide_left(line):
    '''
    Slide all the numbers in a line to the right
    '''
    result = []
    # replace with your code
    for dummy_i in range(len(line)):
        result.append(0)
    count1 = 0
    count2 = 0
    for nums in line[count1:]:
        for elements in result[count2:]:
            if nums != 0 and elements == 0:
                result[count2] = nums
                count2 += 1
            break
    return result
def add_pairs(line):
    '''
    Add every number once with the other
    '''
    count = 0
    while count < len(line):
        if count+2 > len(line):
            break
        if line[count:count+1] == line[count+1:count+2]:
            line[count] += line[count]
            line[count+1] = 0
        count += 1
    return line
def check_zeroes(grid):
    '''
    Check for zeroes in a grid
    '''
    for rows in grid:
        for col in rows:
            if col == 0:
                return True
    return False
def traverse_grid(entries, direction, num_steps, grid):
    '''
    Move throgh the grid in a specific direction
    and get entries of that direction into 
    a list
    '''
    templ1 = []
    templ2 = []
    for cell in entries:
        for step in range(num_steps):
            row = cell[0] + step * direction[0]
            col = cell[1] + step * direction[1]
            templ2.append(grid[row][col])
        templ1.append(templ2)
        templ2 = []
    return templ1
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self.reset()
        self._upp = list_creator(self._grid_height, self._grid_width, 1)
        self._down = list_creator(self._grid_height, self._grid_width, 2)
        self._left = list_creator(self._grid_height, self._grid_width, 3)
        self._right = list_creator(self._grid_height, self._grid_width, 4)
        self._dic = {UP: self._upp, DOWN: self._down, LEFT: self._left, RIGHT: self._right}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ''
        for row in range(len(self._grid)):
            string += str(self._grid[row]) + '\n'

        return string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        changed = False
        if direction == 3 or direction == 4:
            steps = self._grid_width
        else:
            steps = self._grid_height
        traverse = OFFSETS[direction]
        entries = self._dic[direction]
        templ = []
        for line in traverse_grid(entries, traverse, steps, self._grid):
            templ.append(merge(line))
        new_entries = list_creator(len(templ), len(templ[0]), direction)
        if direction == 3 or direction == 4:
            new_steps = len(templ[0])            
        else:
            new_steps = len(templ)
        new_templ = traverse_grid(new_entries, traverse, new_steps, templ)
        print new_templ
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] != new_templ[row][col]:
                    changed = True
                self.set_tile(row,col,new_templ[row][col])
        if changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        prob = random.randrange(10)
        if prob <9:
            num = 2
        else:
            num = 4
        
        if check_zeroes(self._grid):
            count = 0
            while count <1:
                random_row = random.randrange(0,self.get_grid_height())
                random_col = random.randrange(0,self.get_grid_width())
                if self._grid[random_row][random_col] == 0:
                    self.set_tile(random_row,random_col, num)
                    count += 1

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]
#my = TwentyFortyEight(4, 4)


poc_2048_gui.run_gui(TwentyFortyEight(4, 5))
