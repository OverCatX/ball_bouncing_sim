import turtle
from ball import Ball
import random

class BallRun:

    def __init__(self):
        self.num_balls = int(input("Number of balls to simulate: "))
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        self.ball = Ball(self.num_balls, self.ball_radius, self.canvas_width, self.canvas_height)

    def run(self):
        while True:
            turtle.clear()
            self.ball.draw_border()
            for i in range(self.num_balls):
                self.ball.draw_ball(i)
                self.ball.move_ball(i)
                self.ball.update_ball_velocity(i, self.canvas_width, self.canvas_height)
            turtle.update()
        turtle.done()


ballrun = BallRun()
ballrun.run()