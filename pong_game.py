# Code by amotef@gmail.com

# Pong game (using Turtle)

# Step-by-Step:
# Step 1- Create two paddles A and B on the left and right side of the screen.
# Step 2- Create a ball.
# Step 3- Create an event to move the paddle vertically on pressing a certain key.
# Step 4- Create the function to update the score after each player misses a collision.

import turtle
 
# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

