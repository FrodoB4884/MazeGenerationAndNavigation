import turtle
import random
from MazeClass import Maze
import math
import sys

class MazeGenerator:
    def __init__(self, columns, rows, animate_creation=False, animation_stepping=5):
        self.maze = Maze(columns, rows)
        sys.setrecursionlimit(len(self.maze.grid) * len(self.maze.grid[0]))
        
        self.animate_creation = animate_creation
        self.animation_stepping = animation_stepping
        
        self.step = 0
        self.start_point = None
        self.end_point = None
        # store all visited cells during DFS
        self.visited_cells = []

        # makes sure maze fills to edge
        start_cell = (random.randint(0, columns - 1), random.randint(0, rows - 1))
        while start_cell[0] % 2 != 0 or start_cell[1] % 2 != 0:
            start_cell = (random.randint(0, columns - 1), random.randint(0, rows - 1))

        # set the start point
        self.start_point = start_cell  
        self.maze.start_point = self.start_point
        
        # run DFS and start recursion
        self.dfs(start_cell[0], start_cell[1])

        # after DFS, find the farthest cell from the start point to set end point
        self.end_point = self.find_farthest_cell(self.start_point)
        self.maze.end_point = self.end_point

        self.maze.display()

    # recursive function for generation using depth first search
    def dfs(self, x, y):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(directions)

        for direction in directions:
            new_x = x + direction[0] * 2
            new_y = y + direction[1] * 2

            if self.maze.within_maze(new_x, new_y) and self.maze.grid[new_y][new_x] == 1:
                self.maze.grid[y + direction[1]][x + direction[0]] = 0
                self.maze.grid[new_y][new_x] = 0

                # store the current cell as visited
                self.visited_cells.append((new_x, new_y))

                self.step += 1

                # if set to animate then it will display every few steps.
                # not every step for performance reasons
                if self.animate_creation and self.step % self.animation_stepping == 0:
                    self.maze.display()

                self.dfs(new_x, new_y)

    # Find the farthest cell from the start point
    def find_farthest_cell(self, start):
        max_distance = 0
        farthest_cell = start

        for cell in self.visited_cells:
            dist = self.manhattan_distance(start, cell)
            if dist > max_distance:
                max_distance = dist
                farthest_cell = cell

        return farthest_cell

    # Calculate Manhattan distance between two points
    def manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
