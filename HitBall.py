# import turtle for game structure
import turtle 

# Creating a screen for the game
win = turtle.Screen()

# Adding a title
win.title("HitBall by DevoAbhi!")

# Adding background color
win.bgcolor("green")

# Giving a basic widht and height to the screen
win.setup(width=800, height=600)

# This is added so that there is no update in the screen. This enables faster and smoother gameplay
win.tracer(0) 

# Paddle A graphics
paddle_a = turtle.Turtle()

#This is speed of animation. 0 is the fastest upto 10
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color("brown")

# This makes sure that the object created does not draw 
# anyting on the window
paddle_a.penup()

# Give shape to the object - Our basic object has a shape of 20px-20px, so stretch-wid=5 means 5 times the default
paddle_a.shapesize(stretch_wid=7, stretch_len=1)

# Position of the object 
paddle_a.goto(-365, 0)

# Paddle B graphics
paddle_b = turtle.Turtle()

#This is speed of animation. 0 is the fastest upto 10
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color("brown")

# This makes sure that the object created does not draw 
# anyting on the window
paddle_b.penup()

# Give shape to the object - Our basic object has a shape of 20px-20px, so stretch-wid=5 means 5 times the default
paddle_b.shapesize(stretch_wid=7, stretch_len=1)

# Position of the object 
paddle_b.goto(365, 0)

# Main game loop
while True:
    win.update()