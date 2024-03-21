from turtle import *

#we want to paint a house

#step one: draw a square 


penup()
goto(0, -100)
pendown()


speed(100)
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
goto(200, 100)
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
goto(15, 65)
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
goto(185, 65)
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

#starting second house

#start with the square

penup()
goto(-400, -100)
pendown()


color("red")


right(90) 
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)


#end of a square


#we are going to draw a door

penup()
goto(-330, -100)
pendown()


color("blue")


begin_fill()


left(180)
forward(80)
right(90)
forward(60)
right(90)
forward(80)

end_fill()

#we finished the door we are going to start roof now


penup()
goto(-200, 100)
pendown()



color("black")
begin_fill()



right(150)
forward(200)
left(120)
forward(200)
end_fill()

#we finished the door

#we are gonna start windows now this is  first window


penup()
goto(-385, 65)
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

#finished first window, going to start second window


penup()
goto(-215, 65)
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

#we finished second window


















#we finished second house so we are going to make third one


penup()
goto(400, -100)
pendown()



color("orange")


right(90) 
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)


#end of a square




#we are going to draw a door


penup()
goto(470, -100)
pendown()


color("red")


begin_fill()


left(180)
forward(80)
right(90)
forward(60)
right(90)
forward(80)

end_fill()

#end of door

#start of roof


penup()
goto(600, 100)
pendown()



color("black")
begin_fill()



right(150)
forward(200)
left(120)
forward(200)
end_fill()

#we finished the door

#start of first window


penup()
goto(415, 65)
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

#finished first window

#start of second window




penup()
goto(585, 65)
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


#end of second window



#we are going to add some grass now



penup()
goto(-800, -100)
pendown()

color("green")
begin_fill()


right(90)
forward(1600)
right(90)
forward(500)
right(90)
forward(1600)
right(90)
forward(500)

end_fill()

#finished grass


#lets add some trees

penup()
goto(-100, -150)
pendown()


color("brown")
begin_fill()
 

forward(150)
right(90)
forward(35)
right(90)
forward(150)
right(90)
forward(35)


end_fill()


right(90)
forward(120)

color("green")
begin_fill()


left(90)
forward(80)
right(90)
forward(60)
right(90)
forward(60)
left(90)
forward(40)
right(90)
forward(68)
right(90)
forward(40)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(150)



end_fill()

right(90)




#first tree


penup()
goto(200, -200)
pendown()


color("brown")
begin_fill()
 

forward(150)
right(90)
forward(35)
right(90)
forward(150)
right(90)
forward(35)


end_fill()


right(90)
forward(120)

color("green")
begin_fill()


left(90)
forward(80)
right(90)
forward(60)
right(90)
forward(60)
left(90)
forward(40)
right(90)
forward(68)
right(90)
forward(40)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(150)



end_fill()






#second tree

right(90)

penup()
goto(400, -180)
pendown()


color("brown")
begin_fill()
 

forward(150)
right(90)
forward(35)
right(90)
forward(150)
right(90)
forward(35)


end_fill()


right(90)
forward(120)

color("green")
begin_fill()


left(90)
forward(80)
right(90)
forward(60)
right(90)
forward(60)
left(90)
forward(40)
right(90)
forward(68)
right(90)
forward(40)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(150)



end_fill()



#third tree

right(90)

penup()
goto(-500, -200)
pendown()


color("brown")
begin_fill()
 

forward(150)
right(90)
forward(35)
right(90)
forward(150)
right(90)
forward(35)


end_fill()


right(90)
forward(120)

color("green")
begin_fill()


left(90)
forward(80)
right(90)
forward(60)
right(90)
forward(60)
left(90)
forward(40)
right(90)
forward(68)
right(90)
forward(40)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(150)



end_fill()




#forth tree

right(90)


penup()
goto(700, -150)
pendown()


color("brown")
begin_fill()
 

forward(150)
right(90)
forward(35)
right(90)
forward(150)
right(90)
forward(35)


end_fill()


right(90)
forward(120)

color("green")
begin_fill()


left(90)
forward(80)
right(90)
forward(60)
right(90)
forward(60)
left(90)
forward(40)
right(90)
forward(68)
right(90)
forward(40)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(150)



end_fill()











exitonclick()