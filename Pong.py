import turtle
from math import *
import winsound

class PongClass():
    def __init__(self):
        self.a=self.b=0

        self.window=turtle.Screen()
        self.SetWindow()

        self.pen_a=turtle.Turtle()
        self.PaddleA()

        self.pen_b=turtle.Turtle()
        self.PaddleB()

        self.pen_c = turtle.Turtle()
        self.WritePonitA()
        self.a_lost = False

        self.pen_d = turtle.Turtle()
        self.WritePointB()
        self.b_lost = False

        self.ball=turtle.Turtle()
        self.Ball()


    def SetWindow(self):
        self.window.title(" " * 110 + "Pong")
        self.window.setup(width=800, height=600)
        self.window.bgcolor("#000000")
        self.window.tracer(0)
        self.point_a = self.window.textinput("Player 1", "Enter Name:")
        self.point_b = self.window.textinput("Player 2", "Enter Name:")
        self.window._write(pos=(0, self.window.window_height() // 2.2), txt=f" {self.point_a}   |   {self.point_b} ", align="center", font=None, pencolor="#ffffff")
    def PaddleA(self):
        self.pen_a.color("#ffffff")
        self.pen_a.shape("square")
        self.pen_a.shapesize(5, 1)
        self.pen_a.penup()
        self.pen_a.goto(-300, 0)
    def PaddleB(self):
        self.pen_b.color("#ffffff")
        self.pen_b.shape("square")
        self.pen_b.shapesize(5, 1)
        self.pen_b.penup()
        self.pen_b.goto(300, 0)
    def Ball(self):
        self.ball.color("#ffffff")
        self.ball.shape("circle")
        self.ball.penup()
    def WritePonitA(self):
        self.pen_c.color("#ffffff")
        self.pen_c.penup()
        self.pen_c.hideturtle()
        self.pen_c.goto(-15, self.window.window_height() // 2.4)
        self.pen_c.write(self.a)
    def WritePointB(self):
        self.pen_d.color("#ffffff")
        self.pen_d.penup()
        self.pen_d.hideturtle()
        self.pen_d.goto(10, self.window.window_height() // 2.4)
        self.pen_d.write(self.b)
    def go_up_a(self):
        # Upward Movement of Paddle A
        self.y = self.pen_a.ycor()
        if self.pen_a.ycor() <= self.window.window_height() // 2.8:
            self.pen_a.sety(self.y + 20)
    def go_up_b(self):
        # Upward Movement of Paddle B
        self.y = self.pen_b.ycor()
        if self.pen_b.ycor() <= self.window.window_height() // 2.8:
            self.pen_b.sety(self.y + 20)
    def go_dn_a(self):
        # Downward Movement of Paddle A
        self.y = self.pen_a.ycor()
        if -self.pen_a.ycor() <= self.window.window_height() // 2.8:
            self.pen_a.sety(self.y - 20)
    def go_dn_b(self):
        # Downward Movement of Paddle B
        self.y = self.pen_b.ycor()
        if -self.pen_b.ycor() <= self.window.window_height() // 2.8:
            self.pen_b.sety(self.y - 20)
    def PutNewScreen(self):
        self.window.clear()
        self.window = turtle.Screen()
        self.window.title(" " * 110 + "Pong Star")
        self.window.setup(width=800, height=600)
        self.window.bgcolor("#000000")
        self.pen_a.hideturtle()
        self.pen_b.hideturtle()
        self.ball.hideturtle()
    def ShowWinner(self):
        self.pen_1 = turtle.Turtle()
        self.pen_1.color("#ffffff")
        self.pen_1.hideturtle()
        winsound.PlaySound("TaDa.wav", winsound.SND_ASYNC)
        if self.a > self.b:
            self.pen_1.write(arg=f"{self.point_a} Won !", align="Center", font=("Arial", 50, "normal"))
        else:
            self.pen_1.write(arg=f"{self.point_b} Won !", align="Center", font=("Arial", 50, "normal"))

g1=PongClass()

#Paddle Movement
g1.window.listen()
g1.window.onkeypress(g1.go_up_a,"w")
g1.window.onkeypress(g1.go_up_b,"Up")
g1.window.onkeypress(g1.go_dn_a,"s")
g1.window.onkeypress(g1.go_dn_b,"Down")

#Ball Speed
dy = dx =0.4

while g1.a<5 and g1.b<5:
    g1.window.update()

    #moving the ball
    g1.ball.sety(g1.ball.ycor()+dy)
    g1.ball.setx(g1.ball.xcor()+dx)

    #Boundary checking North
    if g1.ball.ycor()>g1.window.window_height()//2.3:
        g1.ball.sety(g1.ball.ycor()-1)
        winsound.PlaySound("Jump.wav", winsound.SND_ASYNC)
        dy=-dy

    # Boundary checking South
    if -g1.ball.ycor()>g1.window.window_height()//2.3:
        g1.ball.sety(g1.ball.ycor()+1)
        winsound.PlaySound("Jump.wav", winsound.SND_ASYNC)
        dy=-dy

    # Boundary checking East
    if g1.ball.xcor()>g1.window.window_width()//2.1:
        g1.ball.sety(0)
        g1.ball.setx(0)
        g1.pen_c.undo()
        g1.a_lost=True
        g1.a+=1
        dx=-dx

    # Boundary checking West
    if -g1.ball.xcor()>g1.window.window_width()//2.1:
        g1.ball.sety(0)
        g1.ball.setx(0)
        g1.pen_d.undo()
        g1.b_lost=True
        g1.b+=1
        dx=-dx

    # co-ordinates of Ball.
    ballx = floor(g1.ball.xcor())
    bally = floor(g1.ball.ycor())

    # co-ordinates of paddels
    penax = floor(g1.pen_a.xcor())
    penay = floor(g1.pen_a.ycor())
    penbx = floor(g1.pen_b.xcor())
    penby = floor(g1.pen_b.ycor())

    #matching position of Paddle A with that of Ball
    pena_ymatch = False
    pena_xmatch = False

    if ballx==penax+20:
      pena_xmatch=True

    if bally <=penay+80 and bally >=penay-80 :
      pena_ymatch = True

    if pena_ymatch and pena_xmatch:
        g1.ball.sety(g1.ball.ycor()+1)
        g1.ball.setx(g1.ball.xcor()+1)
        winsound.PlaySound("Jump.wav", winsound.SND_ASYNC)
        dx=-dx



    #matching position of Paddle B with that of Ball
    penb_ymatch = False
    penb_xmatch = False

    if ballx==penbx-20:
      penb_xmatch=True

    if bally <=penby+80 and bally >=penby-80 :
        penb_ymatch = True

    if penb_ymatch and penb_xmatch:
        g1.ball.sety(g1.ball.ycor()-1)
        g1.ball.setx(g1.ball.xcor()-1)
        winsound.PlaySound("Jump.wav", winsound.SND_ASYNC)
        dx=-dx


    #prints point of Player A
    if g1.a_lost==True:
     g1.pen_c.hideturtle()
     g1.pen_c.undo()
     g1.pen_c.goto(-15, g1.window.window_height() // 2.4)
     g1.pen_c.write(g1.a)
     g1.a_lost=False


    # prints point of Player B
    if g1.b_lost==True:
     g1.pen_d.hideturtle()
     g1.pen_d.undo()
     g1.pen_d.goto(10, g1.window.window_height() // 2.4)
     g1.pen_d.write(g1.b)
     g1.b_lost=False

#clears screen and puts new screen
g1.PutNewScreen()

#shows the name of the winner
g1.ShowWinner()

turtle.done()
