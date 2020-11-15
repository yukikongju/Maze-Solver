#!/usr/bin/python

class Cell():
    """ 
    Parameters:
        - row (int): row in which the cell is located in the grid
        - col (int): col in which the cell is located in the grid
        - has_been_visited (bool): True if the cell has been visited
        - walls (list of bool): check if there are walls around it from [top,
          right, bottom, left]
        - neighbors (list): a list with the indices of the cell's neighbor
    """
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.has_been_visited = has_been_visited
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        self.neighbors = list() # we initialize the neighbor in the maze class




