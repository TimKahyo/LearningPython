import secondary
from secondary import squareAreaOfARectangle
# or you can do this
# from secondary import squareAreaOfARectangle, globalVariable


firstRectangle = squareAreaOfARectangle(5, 10)

print(f"The area of the first rectangle is: {firstRectangle}")
 
print(secondary.globalVariable)