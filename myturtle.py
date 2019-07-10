from turtle import *

shape('turtle')
speed(0)
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

# square(50)
# square(80)
# square()

# Exercise 1-6
# def star(sidelength=100):
#     for i in range(5):
#         forward(sidelength)
#         right(144)

# def spiral_star():
#     length = 5
#     for i in range(480):
#         star(length)
#         right(5)
#         length += 5
# spiral_star()

# Exercise 1-5
# def square_circle():
#     length = 5
#     for i in range(60):
#         square(length)
#         right(5)
#         length += 5
# square_circle()

# Exercise 1-4
# def polygon(sides, sidelength=100):
#     for i in range(sides):
#         forward(sidelength)
#         right(360/sides)
# #polygon(6, 150)
# polygon(16, 75)

# Exercise 1-3
# def triangle(sidelength=100):
#     for i in range(3):
#         forward(sidelength)
#         right(120)
# triangle()

# Exercise 1-2
# for i in range(60):
#     right(5)
#     square()
#     speed(0)

exitonclick()