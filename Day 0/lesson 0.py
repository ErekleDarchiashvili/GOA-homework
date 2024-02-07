from turtle import *

#we want to paint a house

#step one: draw a square 

speed(40)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

forward(70)
color("yellow")
begin_fill()
left(90)
forward(80)        #height of the door
right(90)
forward(60)
right(90)
forward(80)
end_fill()

#start of roof 
penup()         
goto(200, 200)
pendown()

color("brown")       
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()      #end of roof

#drawing first window
penup()
goto(15, 165)
pendown()

color("cyan")
begin_fill()
left(120)
forward(50)
right(90)
forward(50)
right(90) 
forward(50)
right(90)
forward(50)
end_fill()
#end of first window

#drawing second window
penup()
goto(185, 165)
pendown()

color("cyan")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()





exitonclick()