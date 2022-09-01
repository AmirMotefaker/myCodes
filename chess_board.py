# Code by AmirMotefaker

# Chess Board


# Solution 1

# import turtle 
    
# # create screen object
# sc = turtle.Screen()
    
# # create turtle object
# pen = turtle.Turtle()
    
# # method to draw square
# def drawSqr():
    
#   for i in range(4):
#     pen.forward(30)
#     pen.left(90)
    
#   pen.forward(30)
    
   
      
# # Driver Code
# if __name__ == "__main__" :
       
#     # set screen
#     sc.setup(600, 600)
        
#     # set turtle object speed
#     pen.speed(100)
        
#     # loops for board
#     for i in range(8):
        
#       # not ready to draw
#       pen.up()
        
#       # set position for every row
#       pen.setpos(0, 30 * i)
        
#       # ready to draw
#       pen.down()
        
#       # row
#       for j in range(8):
        
#         # conditions for alternative color
#         if (i + j)% 2 == 0:
#           col ='black'
        
#         else:
#           col ='white'
        
#         # fill with given color
#         pen.fillcolor(col)
        
#         # start filling with colour
#         pen.begin_fill()
        
#         # call method
#         drawSqr()
#         # stop filling
#         pen.end_fill()
        
#     # hide the turtle
#     pen.hideturtle()


# Solution 2

import turtle
 
def draw_box(t,x,y,size,fill_color):
    t.penup() # no drawing!
    t.goto(x,y) # move the pen to a different position
    t.pendown() # resume drawing
 
    t.fillcolor(fill_color)
    t.begin_fill()  # Shape drawn after this will be filled with this color!
 
    for i in range(0,4):
        board.forward(size) # move forward
        board.right(90) # turn pen right 90 degrees
 
    t.end_fill() # Go ahead and fill the rectangle!
 
 
def draw_chess_board():
    square_color = "black" # first chess board square is black
    start_x = 0 # starting x position of the chess board
    start_y = 0 # starting y position of the chess board
    box_size = 30 # pixel size of each square in the chess board
    for i in range(0,8): # 8x8 chess board
        for j in range(0,8):
            draw_box(board,start_x+j*box_size,start_y+i*box_size,box_size,square_color)
            square_color = 'black' if square_color == 'white' else 'white' # toggle after a column
        square_color = 'black' if square_color == 'white' else 'white' # toggle after a row!
 
 
board = turtle.Turtle()
draw_chess_board()
turtle.done()
