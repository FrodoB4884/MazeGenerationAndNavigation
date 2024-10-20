from MazeClass import Maze
from MazeGenerator import MazeGenerator

class MazeNavigator:
    def __init__(self, maze, animate_creation=False, animation_stepping=5):
        self.maze = maze

        # make sure maze has a start and end point
        if maze.start_point != None:
            self.start_point = maze.start_point
        else:
            raise Exception("For navigation maze requires a start point")
        if maze.start_point != None:
            self.end_point = maze.end_point
        else:
            raise Exception("For navigation maze requires an end point")

        self.path = self.a_star(animate_creation, animation_stepping)

    def a_star(self, animate_creation=False, animation_stepping=5):
        path = []
        start = self.start_point
        goal = self.end_point
        open_list = [start]  # nodes to be evaluated
        closed_list = []  # evaluated nodes
        g_cost = {start: 0}
        f_cost = {start: MazeNavigator.heuristic(start, goal)}
        came_from = {}
        step = 0

        while open_list:
            # find the node with the lowest f_cost
            lowest_f = min(open_list, key=lambda node: f_cost.get(node, float('inf')))

            # return path if it has reached the goal
            if lowest_f == goal:
                return self.reconstruct_path(came_from, start, goal)

            # move lowest_f from open to closed
            open_list.remove(lowest_f)
            closed_list.append(lowest_f)

            # add valid neighbors to open list and calculate f and g costs
            for neighbor in self.get_neighbors(lowest_f):
                if not self.is_walkable(neighbor) or neighbor in closed_list:
                    continue

                # Tentative g_cost
                tentative_g_cost = g_cost[lowest_f] + 1
                
                if neighbor not in open_list:
                    open_list.append(neighbor)
                elif tentative_g_cost >= g_cost.get(neighbor, float('inf')):
                    continue
                
                # Update g_cost and f_cost
                g_cost[neighbor] = tentative_g_cost
                f_cost[neighbor] = tentative_g_cost + MazeNavigator.heuristic(neighbor, goal)
                came_from[neighbor] = lowest_f
                if animate_creation:
                    self.maze.path_process.append(lowest_f)
                    if step % animation_stepping == 0:
                        self.maze.display()
                    step += 1

        return path  # No path found


    def reconstruct_path(self, came_from, start, goal):
        path = []
        current = goal

        while current != start:
            path.append(current)
            current = came_from.get(current)
            if current is None:  # safety check
                return []  # no valid path
        path.append(start)  # include the start point
        path.reverse()  # reverse to get path from start to goal
        return path


    # using manhattan distance like with the maze generator
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    # gets neighbors within the grid in each direction
    def get_neighbors(self, node):
        neighbors = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for direction in directions:
            next_node = (node[0] + direction[0], node[1] + direction[1])
            if (0 <= next_node[0] < len(self.maze.grid[0])) and (0 <= next_node[1] < len(self.maze.grid)):
                neighbors.append(next_node)
        return neighbors

    # makes code more readable if this logic is a function
    def is_walkable(self, node):
        return self.maze.grid[node[1]][node[0]] == 0
