# -*- coding: utf-8 -*-


from turtle import *


# All of these functions are unusual: they do not have return values!
# This is unusual except in computer graphics, where the rendering of a
# shape is the useful task of the function, rather than computing a value.

# don't forget to lift your pen as you move in preparation for drawing
# and then don't forget to drop the pen once you are prepared to draw
# when possible, I recommend using a for loop

# ------------------------------------------------------------------------------
def drawSquareFL(c, w):
    """Draw a rectilinear square using forward and left.
    Params:
        c (2-tuple): bottom left corner of the square
        w (int):     width of the square, in pixels
    """
    up()
    goto(c)
    down()
    for i in range(2):
        forward(w)
        left(90)
        forward(w)
        left(90)


# ------------------------------------------------------------------------------
def drawSquareFR(c, w):
    """Draw a rectilinear square using forward and right.
    Hint: start by cut and paste of the code from drawSquareFL, then tweak.
    Params:
        c (2-tuple): bottom left corner of the square
        w (int):     width of the square
    """

    up()
    goto(c)
    down()
    for i in range(4):
        forward(w)
        right(90)


# ------------------------------------------------------------------------------
def drawSquareG(c, w):
    """Draw a filled ectilinear square using goto and no forwards.
    This is the preferred way.

    Hint: tuples use indexing just like strings and lists.
    Hint: what are the Cartesian coordinates of the 4 corners?

    Params:
        c (2-tuple): bottom left corner of the square
        w (int):     width of the square"""

    up()
    goto(c)
    down()
    begin_fill()
    goto(c[0] + w, c[1])
    goto(c[0] + w, c[1] + w)
    goto(c[0], c[1] + w)
    goto(c)
    end_fill()


# ------------------------------------------------------------------------------
def drawSquare(c, a, w):
    """Draw a non-rectilinear square (forward is much easier than goto here).
    Hint: small tweak of drawSquareFL
    Params:
        c (2-tuple): bottom left corner of the square
        a (int):     angle of square from +ve x-axis in degrees
                     (initial heading)
        w (int):     width of square
    """
    up()
    goto(c)
    down()
    right(a)
    for i in range(4):
        forward(w)
        right(90)


# ------------------------------------------------------------------------------
def drawTriFL(c, a, L):
    """Draw an equilateral triangle using forward and left.
    Params:
        c (2-tuple): bottom left corner of the triangle
        a (int):     angle of first side from +ve x-axis in degrees
                     (initial heading)
        L (int): length of a side
    """
    up()
    color("red")
    setheading(120)
    goto(c)
    down()
    left(a)
    forward(L)
    left(a)
    forward(L)
    left(a)
    forward(L)


# ------------------------------------------------------------------------------
def drawTri(p, q, r):
    """Draw a filled triangle using goto.  This is the preferred way.
    Params:
        p (2-tuple): 1st vertex
        q (2-tuple): 2nd vertex
        r (2-tuple): 3rd vertex
    """
    up()
    goto(p)
    colormode(255)
    fillcolor(255, 0, 0)
    begin_fill()
    down()
    goto(q)
    goto(r)
    goto(p)
    end_fill()


# ------------------------------------------------------------------------------
def drawFilledTri(c, a, L):
    """Draw an equilateral triangle using forward and right.
    Hint: the code for drawTriFL may be a good starting point for this code
    Params:
        c (2-tuple): bottom left corner of the triangle
        a (int):     angle of first side from +ve x-axis in degrees
                     (initial heading)
        L (int): length of a side
    """
    up()
    colormode()
    setheading(300)
    color("red")
    goto(c)
    down()
    right(a)
    forward(L)
    right(a)
    forward(L)
    right(a)
    forward(L)


# ADD YOUR SQUARE FUNCTION CALLS HERE, drawing in quadrant 1
speed(0)
drawSquareFL((75, 150), 50)
drawSquareFR((100, 100), 50)
drawSquareG((150, 150), 50)
drawSquare((70, 75), 45, 50)

drawTriFL((-100, 200), 120, 50)
drawFilledTri((-50, 100), 120, 50)
drawTri((-200, 100), (-150, 100), (-175, 150))
# I'd suggest making all your squares the same size, say 50 pixels wide
# remember to avoid your other squares

# for faster drawing, increase to speed(5), speed(10) or even speed(0)
# color ('black') # this is the default, so this is technically unnecessary
# drawSquareFL (FILL IN THE ARGUMENTS)
# arguments are values used to call a function, one argument per parameter
# drawSquareFR (FILL IN THE ARGUMENTS)
# drawSquareG (FILL IN THE ARGUMENTS)
# drawSquare (FILL IN THE ARGUMENTS)


# remember to avoid your other triangles
# drawTriFL (FILL IN THE ARGUMENTS)
# drawTri (FILL IN THE ARGUMENTS)
# drawFilledTri (FILL IN THE ARGUMENTS)
# use speed(1) to see your drawing better;
# aesthetically pleasing to remove the turtle from final drawing,
# but you want to show the turtle and its orientation as you draw
  # hold on to the screen, I'm not done admiring my squares
hideturtle()
done()
