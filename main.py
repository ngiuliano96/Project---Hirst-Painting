import random
import turtle
from turtle import Turtle, Screen
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

# print(rgb_colors)


def draw_dot_line(tool, dot, gap, size):
    for _ in range(size):
        tool.dot(dot, random.choice(color_list))
        tool.forward(gap)


# Set tool for drawing
dot_tool = Turtle()
turtle.colormode(255)
dot_tool.speed(0)
dot_tool.penup()
dot_tool.hideturtle()

color_list = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]

# Set starting parameters
tool_pos = [-250, -250]
square_dimension = 10

# Draw the painting
for rows in range(square_dimension):
    dot_tool.setpos(tool_pos[0], tool_pos[1])
    draw_dot_line(dot_tool, 20, 50, square_dimension)
    tool_pos[1] += 50

screen = Screen()
screen.exitonclick()
