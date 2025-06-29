import colorgram
import turtle as t
import random

#colors = colorgram.extract("hirst_dots.png", 40)

# def extract_rgb(colors_object):
#     """Take a list of color objects from colorgram and returns a list of tuples, containing the colors as rgb values."""
#     colors_rgb_list = []
#
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#
#         colors_rgb_list.append((r, g, b))
#
#     return colors_rgb_list

color_list = [(240, 237, 234), (228, 235, 242), (229, 240, 238), (108, 182, 228), (1, 179, 216), (242, 137, 61), (238, 207, 1), (20, 198, 101), (24, 91, 166), (215, 171, 1), (237, 203, 225), (217, 123, 187), (244, 58, 135), (199, 6, 76), (246, 58, 36), (223, 164, 217), (25, 49, 144), (240, 213, 81), (146, 228, 211), (191, 37, 136), (253, 173, 139), (106, 101, 192), (205, 70, 20), (74, 210, 162), (2, 61, 52), (3, 139, 98), (139, 38, 35), (140, 209, 224), (80, 38, 42), (246, 11, 18), (175, 184, 223), (27, 82, 75), (245, 13, 12), (2, 46, 111), (24, 88, 95)]

brush = t.Turtle()
brush.speed("fastest")
brush.hideturtle()

def random_color(color_list):
    """Returns a tuple of a random rgb color from the color_list """
    return random.choice(color_list)

def draw_dots(dot_number_width, dot_number_height, color_list):
    """Takes the number of dots for the width and height as integers and draws them with colors from the color list."""
    t.colormode(255)

    brush.teleport((- (dot_number_width * 50) / 2), (- (dot_number_height * 50) / 2))

    for doth_h in range(dot_number_height):
        current_x, current_y = brush.position()
        brush.teleport((- (dot_number_width * 50) / 2), current_y + 50)

        for dot_w in range(dot_number_width):
            brush.dot(20, random_color(color_list))
            brush.penup()
            brush.forward(50)


draw_dots(10, 10, color_list)

screen = t.Screen()
screen.exitonclick()