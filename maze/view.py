#!/usr/bin/python

class View():
    """ Class that draw and handle the UI part of the maze
    
        Parameters:
            - maze (object → Maze): the maze to draw
            - cell_size (int): width and height of a cell
            - height (int): height of the maze
            - width (int): width of the maze

        Methods:
            - [ ] draw_maze:
    """

    def __init__(self, maze, cell_size):
        self.cell_size = cell_size
        self.height = maze.num_rows * cell_size
        self.width = maze.num_cols * cell_size
        self.maze = maze

    def draw_maze(self):
        """ Function that draw the maze"""

        # plot the walls
    
    



