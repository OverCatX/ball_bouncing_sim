import turtle

class Ball:
    def __init__(self, color, size, xpos, ypos, vx ,vy, dt):
        self.color = color
        self.size = size
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.dt = dt

    def draw_ball(self, i):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color[i])
        turtle.fillcolor(self.color[i])
        turtle.goto(self.xpos[i], self.ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self, i):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[i] += self.vx[i]*self.dt
        self.ypos[i] += self.vy[i]*self.dt


    def update_ball_velocity(self, i, canvas_width, canvas_height):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[i]) > (canvas_width - self.size):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[i]) > (canvas_height - self.size):
            self.vy[i] = -self.vy[i]





