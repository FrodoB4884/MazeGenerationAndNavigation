from MazeClass import Maze
from MazeGenerator import MazeGenerator
from PathfindingAlgorithm import MazeNavigator

maze = MazeGenerator(49, 49).maze
navigator = MazeNavigator(maze)
maze.solution = navigator.path
maze.display()
