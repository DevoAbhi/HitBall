# import turtle for game structure
import turtle 

# Creating a screen for the game
win = turtle.Screen()

# Adding a title
win.title("HitBall by DevoAbhi!")

# Adding background color
win.bgcolor("black")

# Giving a basic widht and height to the screen
win.setup(width=800, height=600)

# This is added so that there is no update in the screen. This enables faster and smoother gameplay
win.tracer(0) 

while True:
    win.update()