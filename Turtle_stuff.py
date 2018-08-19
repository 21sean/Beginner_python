

from turtle import *

# ------------------------------------------------------------------------------
# DO NOT CHANGE THIS FUNCTION
def drawCorners (corners):

    """Draw a set of corners in the present colour.
    Params: corners (list of int 2-tuples) corners
    """

    for i in range(len(corners)):
        up()
        goto(corners[i])
        down()
        dot(10)
# ------------------------------------------------------------------------------
def cCorners (blc, w):

    """Build a list of the corners of the C maritime flag.
    You should use linear interpolation to compute the corners.
    Remember that each corner is a point,
    so represented in Python as a tuple T of size 2 containing 2 integers,
    where T[0] is the x-coordinate and T[1] is the y-coordinate.
    Review lists and tuples if you need, since you are building 
    a list of tuples.

    Before you write the code, I would draw a picture of the flag and 
    express each of the 12 corners using linear interpolation.
    Then you can attack the Python code with a clear idea of what you are
    trying to do.
    Challenge: can you write the code using 2 for loops? That is most elegant.

    Params: blc (int 2-tuple): bottom left corner of the C flag
    Returns: (list of 2-tuples) corners of the C flag
    """
    up()
    L = []
    for i in range(6):
        L.append((blc[0], blc[1]+w*i/5))
        L.append((blc[0]+w, blc[1]+w*i/5))
    return L
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

def drawLineForward (p, a, L):

    """Draw a line segment using forward.
    Params:
        p (2-tuple): starting point of the line segment
        a (int): heading of the line (in degrees from +ve x-axis)
        L (int): length of the line, in pixels
    """
    up()
    setheading(a)
    goto(p)
    down()
    forward(L)

# ------------------------------------------------------------------------------
def drawLine (p, q):
    
    """Draw a line segment using goto.  This is the preferred way.
    Params:
        p (2-tuple): first endpoint of the line segment
        q (2-tuple): second endpoint of the line segment
    """

    up()
    goto(p)
    down()
    goto(q)
    up()
# ------------------------------------------------------------------------------
def drawManyLines (c, L):
    
    """Draw 10 vertical and 10 horizontal line segments.
    Optimally on a regular grid.
    Hint: sketch out your grid on a piece of paper and plan your attack.
    Hint: you already have code for drawing a line segment.
    Params: 
        c (2-tuple): bottom left corner of grid
        L (int): length of each line
    """
    goto(c)
    for i in range(10):
        i=i+1
        up()
        goto(c[0]+10, c[1]+L*i/10)
        down()
        forward(L-10)
    setheading(90)
    for i in range (10):
        i =i+1
        up()
        goto(c[0]+L*i/10, c[1]+10)
        down()
        forward(L -10)



# ------------------------------------------------------------------------------
def drawRegular (n, c, L):
    
    """Draw a filled regular polygon with n sides.

    Hint 1: what is the interior angle of a regular n-gon?
    Relevant fact: the sum of the interior angles of an n-gon is 
    (n-2)*180 degrees (or (n-2)pi radians).  
    For example, 180 degrees ( pi radians) for a triangle.
                 360 degrees (2pi radians) for a square.
                 540 degrees (3pi radians) for a pentagon.
    Hint 2: use left and forward for a simpler solution

    Params: 
        n (int): # of sides of your regular polygon
        c (2-tuple): bottom left corner of polygon
        L (int): length of each edge
    """

    # ADD CODE HERE
    
# ------------------------------------------------------------------------------
speed(0)
# HERE IS THE C CORNERS CALL: note that we are drawing in the first quadrant
# DON'T CHANGE THESE 2 CALLS
color ('DarkViolet')
drawCorners (cCorners ((10, 50), 100))
# another call for good measure, and to establish the code's flexibility:
color ('DodgerBlue')
drawCorners (cCorners ((130, 50), 125))

# ADD YOUR LINE FUNCTION CALLS HERE
# in quadrant 3 (I'll leave quadrant 2 for your M flag if you do that challenge)
color('green')

drawLineForward((-200, -200), 360, 100)
drawLine((-200,-185),(-100,-185))
drawManyLines((-190,-190), 100)

# ADD YOUR REGULAR POLYGON FUNCTION CALL HERE
# draw in quadrant 4
# this is an extra challenge
color('blue')
# drawRegular (FILL IN PARAMETERS HERE)

hideturtle() # aesthetically pleasing to remove the turtle from final drawing,
             # but you want to show the turtle and its orientation as you draw
done() # hold on to the screen, I'm not done admiring the corners
