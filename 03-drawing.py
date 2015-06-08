import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("blue")

	larry = turtle.Turtle()
	larry.shape("turtle")
	larry.color("green")
	#larry.speed(2)
	x=0
	while (x<4):
		larry.forward(100)
		larry.right(90)
		x+=1
	window.exitonclick()

draw_square()