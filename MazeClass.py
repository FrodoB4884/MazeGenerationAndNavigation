import turtle
import math

class Maze:
    def __init__(self, columns, rows):
        self.grid = [[1] * columns for _ in range(rows)]
        self.graphic = turtle.Turtle()
        self.graphic.ht()

        # autosize to fit screen
        height_fit = (turtle.window_height() / (len(self.grid) + 2))
        width_fit = (turtle.window_width() / (len(self.grid[0]) + 2))

        fit = min(height_fit, width_fit)

        self.display_size = fit - (0.1 * fit)
        
        self.start_point = None  # store start coordinates
        self.end_point = None  # store end coordinates
        self.solution = None # store A Star path solution
        self.path_process = [] # stores paths that are tried in the a star process

        self.window = self.graphic.screen
        self.window.tracer(0)  # Manually control updates

        self.graphic.speed(0)

    def within_maze(self, x, y):
        return (0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid))               

    # display method with turtle
    def display(self):
        self.graphic.clear()
        offset_x = -(len(self.grid[0]) / 2) * self.display_size
        offset_y = -(len(self.grid) / 2) * self.display_size
        self.draw_grid(offset_x, offset_y)
        self.draw_frame(offset_x, offset_y)

        cy = 0
        for y in self.grid:
            cx = 0
            for x in y:
                if x == 1:
                    self.draw_square(cx, cy, offset_x, offset_y, "black")
                cx += 1
            cy += 1

        # for animating a star process
        if self.path_process != []:
            for coordinate in self.path_process:
                self.draw_square(coordinate[0], coordinate[1], offset_x, offset_y, "light blue")            

        # draw the solution path
        if self.solution != None:
            for coordinate in self.solution:
                self.draw_square(coordinate[0], coordinate[1], offset_x, offset_y, "blue")

        # Draw the start and end points
        if self.start_point != None:
            start_x, start_y = self.start_point
            self.draw_square(start_x, start_y, offset_x, offset_y, "red")

        if self.end_point != None:
            end_x, end_y = self.end_point[0], self.end_point[1]
            self.draw_square(end_x, end_y, offset_x, offset_y, "green")
                
        self.window.update()

    # method to create a square
    def draw_square(self, x, y, offset_x, offset_y, color):
        self.graphic.penup()
        self.graphic.setx(x * self.display_size + offset_x)
        self.graphic.sety(y * self.display_size + offset_y)
        self.graphic.seth(0)

        self.graphic.fillcolor(color) 
        self.graphic.begin_fill() 
        self.graphic.pendown()

        for _ in range(4):
            self.graphic.forward(self.display_size)
            self.graphic.left(90)

        self.graphic.end_fill()
        self.graphic.penup()

    # method for drawing the grid
    def draw_grid(self, offset_x, offset_y):
        self.graphic.penup()
        self.graphic.setx(offset_x)
        self.graphic.sety(offset_y)
        self.graphic.seth(0)

        self.graphic.pendown()
        for _ in range(len(self.grid[0])):
            self.graphic.left(90)
            self.graphic.forward(len(self.grid) * self.display_size)
            self.graphic.left(180)
            self.graphic.forward(len(self.grid) * self.display_size)
            self.graphic.left(90)
            self.graphic.forward(self.display_size)

        self.graphic.left(90)

        for _ in range(len(self.grid)):
            self.graphic.left(90)
            self.graphic.forward(len(self.grid[0]) * self.display_size)
            self.graphic.left(180)
            self.graphic.forward(len(self.grid[0]) * self.display_size)
            self.graphic.left(90)
            self.graphic.forward(self.display_size)

        self.graphic.left(90)
        self.graphic.forward(len(self.grid[0]) * self.display_size)
        self.graphic.penup()

    # method for drawing the frame
    def draw_frame(self, offset_x, offset_y):
        for x in range(len(self.grid[0])+2):
            self.draw_square(x-1, -1, offset_x, offset_y, "black")
        for x in range(len(self.grid[0])+2):
            self.draw_square(x-1, len(self.grid), offset_x, offset_y, "black")

        for y in range(len(self.grid)):
            self.draw_square(-1, y, offset_x, offset_y, "black")
        for y in range(len(self.grid)):
            self.draw_square(len(self.grid[0]), y, offset_x, offset_y, "black")
        
        
        
