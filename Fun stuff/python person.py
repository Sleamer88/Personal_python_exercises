from turtle import *

color("purple","beige")
begin_fill()
pensize(7)
# legs
forward(40)
right(90)
forward(170)
right(90)
forward(40)
right(90)
forward(170)
left(90)
forward(50)
left(90)
forward(170)
left(90)
forward(40)
left(90)
forward(170)
left(90)
forward(40)
right(90)
# left side body
forward(270)
# left arm
left(150)
forward(160)
left(90)
forward(20)
left(90)
forward(125)
left(30)
# neck
forward(45)
right(90)
forward(35)
left(90)
forward(20)
left(180)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(180)
forward(20)
left(90)
forward(35)
left(180)
forward(35)
right(90)
forward(20)
# head
circle(10, 180, 8)
forward(20)
left(90)
forward(55)
right(90)
forward(5)
# right arm
left(30)
forward(160)
right(90)
forward(20)
right(90)
forward(125)
left(150)
# right side body
left(180)
forward(40)
left(180)
forward(270)

end_fill()
mainloop()