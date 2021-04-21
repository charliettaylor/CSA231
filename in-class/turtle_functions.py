import turtle
from typing import Callable, OrderedDict

X_LENGTH = 500
Y_LENGTH = 500
Y_RATE = 0.25


def relative_goto(t: turtle.Turtle, zero_x: float, zero_y: float):
    """
    given 0, 0 coordinate, draw relative position
    :param t: turtle object
    :param zero_x: top left x coordinate
    :param zero_y: top left y coordinate
    :return: A function
    """

    def goto(x: float, y: float) -> None:
        t.goto(zero_x + x, zero_y + y)

    return goto


def jump(t: turtle.Turtle, x: float, y: float) -> None:
    """
    Turtle object jump to x, y without drawing
    :param t: turtle object
    :param x: x position
    :param y: y position
    :return: None
    """
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_frame(t: turtle.Turtle, rg: Callable) -> None:
    """
    Draw the frame for the graph
    :param t: turtle object
    :param rg: Callable relative_goto function
    :return: None
    """
    t.pen(pencolor="black", pensize=4)
    t.penup()
    rg(0, Y_LENGTH)
    t.seth(90)
    t.stamp()
    t.pendown()
    rg(0, 0)
    rg(X_LENGTH, 0)
    t.seth(0)
    t.stamp()


def scale_factor(cities_data: OrderedDict, years: int, rate: float):
    compare = []
    for c in cities_data:
        compare.append(int(cities_data[c][-1]))
    max_rate = max(compare)
    max_y = 0
    for y in range(int(years)):
        max_y += max_rate
        max_y *= 1 + float(rate)
    
    return Y_LENGTH / max_y