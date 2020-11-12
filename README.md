## Maze Solver

### What is this project about?

I'm trying to implement path finder algorithm that solve generated maze using
data structures and algorithms I have learned.

### Dissecting the Project

#### Step #1: Generating the Maze

I want to generate different maze difficulty based on its size and how many
dead ends it has. 

- [ ] Method #1: Implementation with a Stack and looking at nearest unvisited
neighbor

As depicted by javidx9 in his youtube videos
[https://www.youtube.com/watch?v=Y37-gB83HKE], one way to build a maze is to,
from a given node, link it to its unvisited neighbor until none can be reached.

Everytime we link a node, we add it onto a stack so that when we reach a node
that has no unvisited neighbor, we can "backtrack" by popping the nodes on the
top of the stack until we find one that has an unvisited neighbor that we can
link to the maze. 

We know when to end the algorithm when all nodes are visited ie when the stack
is empty and there is no more neighbor left to explore

#### Step #2: Add a GUI

We want to show the maze and how the algorithm works

#### Step #3: Solve the maze by implementing path finding algorithm

Algorithms to implement:

- [ ] Dijkstra
- [ ] Ford-Fulkerson
- [ ] Using Linear Programming and connectivity
- [ ] BFS
- [ ] DFS
- [ ] Backtracking
- [ ] Floyd-Warshall
- [ ] A* Search

More: Add a quick description on how the algorithm works?



### More - Solving a Maze with Reinforcement Learning



### More - Generating a Maze using Reinforcement Learning or Genetic Algorithm

I'm not quite sure how I'll implement that yet, bu I'm thinking on using the
website http://www.mazegenerator.net/ to generate my dataset. However, I still
have to find a way to quantify how good the maze generated is ie the metric
I'll use to evaluate the "goodness" of the generated maze.

- [x] Step #1: Create the dataset by fetching the generated maze from http://www.mazegenerator.net/

I'll use selenium, a python's module: https://www.geeksforgeeks.org/how-to-click-a-button-on-webpage-using-selenium/

### More - Use Computer Vision to solve a maze with only its picture


### Sources

- https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
- http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
- https://github.com/jostbr/pymaze
