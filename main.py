

from turtle import *
import math
Test = Turtle()
Test.screen.setup(800, 800)
def ang( id , count = 5 , Rad = 10 ):
    ang_ = 2 / count * id * 3.1415 # Радианах 
    posX =  Rad * math.sin( ang_ )
    PosY =  Rad * math.cos( ang_ )    
    return posX , PosY
def rectangle(w, h):
    count = 3
    Radius = 66 
    for i in range( 0 , count + 1):
        x , y = ang( i ,  count = count , Rad = Radius )
        Test.goto( x , y )
rectangle(320, 200)
Test.screen.exitonclick()
Test.screen.mainloop()

rectangle(320, 200)
Test.screen.exitonclick()
Test.screen.mainloop()
