#!/usr/bin/python

from enum import Enum

class Algorithms(object):

    #  @unique
    class Generate(Enum):
        """ Enum of algorithms used to generate maze"""
        BACKTRACKING = "Recursive backtracking algorithm"
        HUNT         = "Hunt and kill algorithm"
        ELLER        = "Eller's algorithm"
        SIDEWINDER   = "Sidewinder algorithm"
        PRIM         = "Prim's algorithm"
        KRUSKAL      = "Kruskal's algorithm"

    #  @unique
    class Solve(Enum):
        """ Enum of algorithms used to solve maze"""
        DEPTH   = "Depth-first search"
        BREADTH = "Breadth-first search"
        DIJKSTRA = "Dijstra's Algorithm"
        BELLMAN_FORD = "Bellman-Ford's Algorithm"
        LINEAR_PROGRAMMING = "Linear Programming"
        A_SEARCH = "A* Search Algorithm"

