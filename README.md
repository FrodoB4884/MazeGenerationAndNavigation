# MazeGenerationAndNavigation
This is an A Level style project that generates a maze using DFS and then solves it using A Star. These process are done using recursion rather than iteration and I have separated the main components of the project into objects, the maze class, the maze generator class and the maze navigator class.
I have implemeted the graphics using Turtle, and you can choose to view the creation and solution of the maze step by step by setting the animate_creation property of the maze generation class and maze navigation class during their initialization to true like so:
```
from MazeClass import Maze
from MazeGenerator import MazeGenerator
from PathfindingAlgorithm import MazeNavigator

maze = MazeGenerator(49, 49, True).maze
navigator = MazeNavigator(maze, True)
maze.solution = navigator.path
maze.display()
```
![Video of animated maze creation](https://github.com/user-attachments/assets/d16314d5-f49c-40d6-8328-7f5f92882217)
You can also set how many steps of creation or solution it goes through before each display, the default is 5. The lower it is the slower and more detailed it will be, and higher is the opposite.
```
from MazeClass import Maze
from MazeGenerator import MazeGenerator
from PathfindingAlgorithm import MazeNavigator

maze = MazeGenerator(49, 49, True, 20).maze
navigator = MazeNavigator(maze, True, 20)
maze.solution = navigator.path
maze.display()
```
()
