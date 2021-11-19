import turtle as trtl

drawer = trtl.Turtle()
wall_length = 300
drawer.setposition(300,300)
drawer.setheading(-90)
def draw_maze():
	global wall_length
	for x in range(10):
		for x in range(3):
			drawer.forward(wall_length)
			drawer.right(90)
		wall_length -= 10

draw_maze()

	
wn = trtl.Screen()
wn.mainloop()