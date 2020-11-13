#!/usr/bin/python

class Maze():
    """ Class used to generate the maze 
        
        Parameters:
            - num_rows (int): number of rows the maze has
            - num_cols (int): number of columns the maze has
            - grid_size (int): number of cells in the grid 
            - grid (list): a list with all the cells that makes up the grid 
            - path (stack): keep track of the visited cells to backtrack when
              we reach a cell with no unvisited neighbor
        
        Methods:
            - [ ] 
    """
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid_size = num_rows * num_cols


    def generate_empty_grid(self):
        """ Function which create the grid with all the cells
        
            Return: a 2D array made of 'Cell' with all their walls
        """
        # we create an empty list that we fill in with cell
        grid = list() 
        for i in range(num_rows):
            grid.append(list())
            for j in range(num_cols):
                grid[i].append(Cell(i,j))
        return grid


        



