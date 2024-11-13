import turtle
import random

class Ball:
    def __init__(self, num_balls, ball_radius, canvas_width, canvas_height):
        self.ball_color = []
        self.ball_radius = ball_radius
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.dt = 1
        for i in range(num_balls):
            self.xpos.append(random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def draw_ball(self, i):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.ball_color[i])
        turtle.fillcolor(self.ball_color[i])
        turtle.goto(self.xpos[i], self.ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def move_ball(self, i):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[i] += self.vx[i]*self.dt
        self.ypos[i] += self.vy[i]*self.dt


    def update_ball_velocity(self, i, canvas_width, canvas_height):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[i]) > (canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[i]) > (canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]





