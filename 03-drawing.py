import turtle

def draw_circle():
	larry = turtle.Turtle()
	larry.shape("turtle")
	larry.color("red")
	#larry.speed(2)
	larry.circle(50)

def draw_pentagon():
	jimmy = turtle.Turtle()
	jimmy.shape("turtle")
	jimmy.color("yellow")
	#larry.speed(2)
	x=0
	while (x<5):
		jimmy.forward(100)
		jimmy.right(72)
		x+=1

def draw_square():
	barry = turtle.Turtle()
	barry.shape("turtle")
	barry.color("green")
	#larry.speed(2)
	x=0
	while (x<4):
		barry.forward(100)
		barry.right(90)
		x+=1

def draw_triangle():
	harry = turtle.Turtle()
	harry.shape("turtle")
	harry.color("white")
	#larry.speed(2)
	x=0
	while (x<3):
		harry.forward(100)
		harry.right(120)
		x+=1

def draw_stuff():
	window = turtle.Screen()
	window.bgcolor("blue")

	draw_circle()
	draw_pentagon()
	draw_square()
	draw_triangle()

	window.exitonclick()

draw_stuff()