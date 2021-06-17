import turtle
import time
import random

b = 0

# SCREEN

display = turtle.Screen()
display.title("Pong Game")
display.bgcolor("black")
display.setup(width = 700, height = 500)

# WALLS

# WALL 1
wall1 = turtle.Turtle()
wall1.shape('square')
wall1.color('blue')
wall1.speed(0)
wall1.shapesize(stretch_len = 1, stretch_wid = 4)
wall1.penup()
wall1.goto(-300,0)

# WALL 1 MOVEMENT
def wall1up():
    y = wall1.ycor()
    y += 20
    wall1.sety(y)
def wall1down():
    y = wall1.ycor()
    y -= 20
    wall1.sety(y)



# WALL 2 
wall2 = turtle.Turtle()
wall2.shape('square')
wall2.color('blue')
wall2.speed(0)
wall2.shapesize(stretch_len = 1, stretch_wid = 4)
wall2.penup()
wall2.goto(300,0)

# WALL 2 MOVEMENT
def wall2up():
    y = wall2.ycor()
    y += 20
    wall2.sety(y)
def wall2down():
    y = wall2.ycor()
    y -= 20
    wall2.sety(y)

# WALL's REACTION ON KEYPRESS
display.listen()

display.onkeypress(wall1up,"w")
display.onkeypress(wall1down,"s")
display.onkeypress(wall2up,"Up")
display.onkeypress(wall2down,"Down")


#BALL
ball = turtle.Turtle()
ball.color('white')
ball.shape('circle')
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx =  random.randint(-10, 5)
ball.dy = random.randint(-5, 10)


# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("red")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 210)
sketch.write("PLAYER A : 0	   PLAYER B : 0",
			align="center", font=("Courier", 24, "normal"))

def fun():

    ball.goto(-1000,-1000)
    wall1.goto(-1000,1000)
    wall2.goto(1000,1000)


    if scoreA > scoreB:
        sketch.clear()
        sketch.goto(0,0)
        sketch.write("CONGRATULATIONS!! \nPLAYER A WON THE GAME", align= "center", font=("Courier", 25, "normal"))
        time.sleep(2)
        
    if scoreA < scoreB:
        sketch.clear()
        sketch.goto(0,0)
        sketch.write("CONGRATULATIONS!! \nPLAYER B WON THE GAME", align= "center", font=("Courier", 25, "normal"))
        time.sleep(2)


# MAIN FUNCTION:

scoreA = 0
scoreB = 0


while True:
    display.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BOUNDARY:
    if ball.ycor() > 240 or ball.ycor() <-240:
        ball.dy *= -1

    # WALL TOUCH:

    if  ball.xcor()<-260 and ball.xcor()>-270 and ball.ycor() > wall1.ycor()-70 and ball.ycor() < wall1.ycor()+70: 
        ball.setx(-260)
        ball.dx *= -1

    if  ball.xcor()>260 and ball.xcor()<270 and ball.ycor() > wall2.ycor()-70 and ball.ycor() < wall2.ycor()+70:
        ball.setx(260)
        ball.dx *= -1

    # SCORE UPDATE:

    if ball.xcor()<-350:
        ball.dx =  random.randint(-10, -3)
        ball.dy = random.randint(-8, -3)
        ball.goto(0,0)
        time.sleep(0.1)
        scoreA += 0
        scoreB += 1
        sketch.clear()
        sketch.write("PLAYER A : {}    PLAYER B : {} ".format(scoreA , scoreB), align = "center" , font=("Courier", 20, "normal"))


    if ball.xcor()>350:
        ball.dx =  random.randint(3, 8)
        ball.dy = random.randint(4, 10)
        ball.goto(0,0)
        time.sleep(0.1)    
        scoreA += 1
        scoreB += 0
        sketch.clear()
        sketch.write("PLAYER A : {}    PLAYER B : {}".format(scoreA , scoreB), align = "center" , font=("Courier", 20, "normal")) 

    if scoreA == 3 or scoreB == 3:
        fun()

        

    

    #   display.onkeypress(wall2down,"Down")