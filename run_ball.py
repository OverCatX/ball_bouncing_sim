import turtle
from ball import Ball
import random

class BallRun:

    def __init__(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        self.dt = 1

    # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
    def adjust_ball(self, num_balls):
        for i in range(num_balls):
            self.xpos.append(random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

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

    def run(self):
        num_balls = int(input("Number of balls to simulate: "))
        self.adjust_ball(num_balls)
        while True:
            turtle.clear()
            self.draw_border()
            ball = Ball(self.ball_color, self.ball_radius, self.xpos, self.ypos, self.vx, self.vy, self.dt)
            for i in range(num_balls):
                ball.draw_ball(i)
                ball.move_ball(i)
                ball.update_ball_velocity(i, self.canvas_width, self.canvas_height)
            turtle.update()
        turtle.done()


ballrun = BallRun()
ballrun.run()