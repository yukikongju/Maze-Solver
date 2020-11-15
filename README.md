# Maze Solver

A simple app created with python that generate and solve a maze step by step
using a path finding algorithm

## Table of contents
* [Motivation](#motivation)
* [Technologies](#technologies)
* [Features](#features)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Implementation](#implementation)
* [Ressources](#ressources)
* [Acknowledgments](#acknowledgments)

## Motivation


## Technologies

* flask
* opencv-python
* selenium

## Features

to do:
- [ ] Generate the maze
- [ ] Solve the generated maze
- [ ] Select a shortest path algorithm
- [ ] Show the steps for the algorithm used

More:
- [ ] Solve a maze from a picture

Note to self: add screenshot for each features

## Getting Started

### Requirements

* Python 3.7+
* git

### Installation

The first step is to clone the repository in the directory desired. To do so, open your
terminal and navigate to the directory desired using the command ``cd``. To
clone the repository, run the following script in your terminal

```
git clone https://github.com/yukikongju/Maze-Solver
```

Next, install the dependencies needed to run the app by typing the following in
your terminal

```
pip install -r requirements.txt
```

You should be all set to use the app!

## Usage

[todo]



## Implementation

### Generating the Maze from scratch

[Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm) suggest
a bunch of algorithms to generate a maze:

- [x] Recursive Backtracker
- [ ] Randomized Kruskal's algorithm
- [ ] Randomized Prim's algorithm
- [ ] Wilson's algorithm
- [ ] Aldous-Broder algorithm
- [ ] Recursive division method

The one implemented in this app uses the recursive backtracker method.

#### How it works?

We can visualize the maze as a nxn grid, where each cells has 4 walls: top,
right, bottom, left. To make our maze, we just need to figure out which walls
need to be destroyed.

[insert picture of walls]

In the beginning, all cells have their 4 walls. We begin at a random cell,
let's say at index `(0,0)`, and we want to visit one of its unvisited
neighbors. To keep track of the path we took, we will use a stack. When the neighbor
is visited, we set that cell as visited, add it to the stack and
destroyed the wall between the current cell and the neighbor. However, if
a cell has no unvisited neighbor, we have to backtrack by popping the cells in
the stack until we find a cell with an unvisited neighbor. We know we are done
when all cells are visited

Pseudo Code from Wikipedia:
[Insert image of pseudo code]

[insert image of cell and neighbor, and their indexes]

#### The Code

We have a class called ``Cell`` that knows wether its walls are destroyed or
not and wether it has been visited or not

[insert image of class Cell]

We also have a class called `Maze` made of `Cell`

[insert class maze]


### Solving the maze

Solving the maze is done by implementing a path finding algorithm. Luckily,
[Wikipedia](https://en.wikipedia.org/wiki/Pathfinding) also list a bunch of path finding algorithm we can use:

- [ ] Dijkstra
- [ ] Bellman-Ford
- [ ] Floyd-Warshall
- [ ] BFS
- [ ] DFS
- [ ] Backtracking
- [ ] A* Search
- [ ] Linear Programming and Connectivity
- [ ] more ...

### Generating a Maze from a Picture

We first download a bunch of maze picture from the website
http://www.mazegenerator.net/ using selenium. The script can be found in
`fetch_maze_dataset.py`

Then, we use edge detection [to complete]


## Ressources

### Using Selenium
* https://www.geeksforgeeks.org/how-to-click-a-button-on-webpage-using-selenium/

### Maze generation inspiration
* https://en.wikipedia.org/wiki/Maze_generation_algorithm
* https://github.com/jostbr/pymaze
* https://github.com/jsmolka/maze
* https://github.com/nas-programmer/maze-generator
* https://www.youtube.com/watch?v=Y37-gB83HKE

### MVC examples
* https://codereview.stackexchange.com/questions/173872/pygame-flappy-bird-clone-object-oriented

### Path Finding Algorithm
* https://en.wikipedia.org/wiki/Pathfinding

### Writing a proper README.md
* https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project

### Using Ipyiwidgets with matplotlib
* https://kapernikov.com/ipywidgets-with-matplotlib/



## Acknowledgments



