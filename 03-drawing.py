import turtle

def draw_circle(turts):
	turts.circle(50)

def draw_pentagon(turts):
	x=0
	while (x<5):
		turts.forward(100)
		turts.right(72)
		x+=1

def draw_square(turts):
	x=0
	while (x<4):
		turts.forward(100)
		turts.right(90)
		x+=1

def draw_triangle(turts):
	x=0
	while (x<3):
		turts.forward(100)
		turts.right(120)
		x+=1

def draw_circle_square(turts):
	x=0
	while (x<36):
		draw_square(turts)
		turts.right(10)
		x+=1

def draw_stuff():
	window = turtle.Screen()
	window.bgcolor("blue")

	larry = turtle.Turtle()
	larry.shape("turtle")
	larry.color("red")
	#larry.speed(2)
	draw_circle(larry)

	jimmy = turtle.Turtle()
	jimmy.shape("turtle")
	jimmy.color("yellow")
	draw_pentagon(jimmy)

	barry = turtle.Turtle()
	barry.shape("turtle")
	barry.color("green")
	draw_square(barry)

	harry = turtle.Turtle()
	harry.shape("turtle")
	harry.color("white")
	draw_triangle(harry)

	bobby = turtle.Turtle()
	bobby.shape("turtle")
	bobby.color("pink")
	draw_circle_square(bobby)

	window.exitonclick()

draw_stuff()