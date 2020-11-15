#!/usr/bin/python

from enum import Enum

class Maze():
    """ Class used to generate the maze 
        
        Parameters:
            - num_rows (int): number of rows the maze has
            - num_cols (int): number of columns the maze has
            - grid_size (int): number of cells in the grid 
            - grid (list): a list with all the cells that makes up the grid 
            - path (stack): keep track of the visited cells to backtrack when
              we reach a cell with no unvisited neighbor and the current cell
            - generation_algorithm (Enum): the algorithm used to generate
              the maze
            - solution_algorithm (Enum): the algorithm used to solve the maze
        
        Methods:
            - [ ] generate_empty_grid
            - [ ] generate
            - [ ] solve
    """
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid_size = num_rows * num_cols

    class Generate(self):
        """ Enum of algorithms used to generate maze"""
        BACKTRACKING = "Recursive backtracking algorithm"
        HUNT         = "Hunt and kill algorithm"
        ELLER        = "Eller's algorithm"
        SIDEWINDER   = "Sidewinder algorithm"
        PRIM         = "Prim's algorithm"
        KRUSKAL      = "Kruskal's algorithm"

    class Solve(self):
        """ Enum of algorithms used to solve maze"""
        DEPTH   = "Depth-first search"
        BREADTH = "Breadth-first search"
        DIJKSTRA = "Dijstra's Algorithm"
        BELLMAN_FORD = "Bellman-Ford's Algorithm"
        LINEAR_PROGRAMMING = "Linear Programming"
        A_SEARCH = "A* Search Algorithm"



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

    def find_unvisited_neighbor(cell):
        """ Function that check if the cell's neighbor have been visited or not
            
            Return:
                * if cell has unvisited neighbor, return its [row, col]
                * if the cell has no unvisited neighbor, return -1
        '"""
        # add the neighbors if they exist by checking if neighbor are out of bound
        neighbors_indexes = list()
        if cell.row - 1 >= 0 : # check if top neighbor exist
            neighbors.append((cell.row - 1, cell.col)) 
        if cell.col + 1 < num_cols: # check if right neighbor exist
            neighbors.append((cell.row, cell.col + 1))
        if cell.row + 1 < num_rows: # check if bottom neighbor exist
            neighbors.append((cell.row + 1, cell.col))
        if cell.col - 1 < 0 : # check if left neighbor exist
            neighbors.append((cell.row, cell.col - 1))

        # check if neighbor have been visited or not
        for neighbor_index in neighbors_indexes:
            neighbor_row = neighbor_index[0]
            neighbor_col = neighbor_index[1]
            if maze[neighbor_row][neighbor_col].has_been_visited() == False:
                return neighbor_row, neighbor_col

        # if all the neighbor have been visited, return -1
        return -1

    
    def generate(self):
        def 





        



