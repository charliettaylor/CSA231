# Yitian Huang and Charlie Taylor
import random
import sys
from collections import OrderedDict
from datetime import date
import turtle
from turtle_functions import *

FILE_NAME = "localpops.txt"


def print_welcome() -> None:
    """
    print greeting
    :return: None
    """
    print("""----------------------------------------------------
Welcome to the cities population projection programs
                now with turtle!
              by Yitian and Charlie
----------------------------------------------------""")


def read_cities() -> dict:
    """
    read and process cities data from file
    :return: dictionary of cities and its statistics
    """
    print("The cities in our available data set:")
    data = OrderedDict()
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                city_name, city_death, city_born, city_move_in = \
                    line.strip().split(", ")
                data[city_name] = (city_death, city_born, city_move_in,
                    int(city_born) + int(city_move_in) - int(city_death))
    except FileNotFoundError:
        print("No file found")
        raise FileNotFoundError

    return data


def print_cities_data(cities_data: OrderedDict) -> None:
    """
    print cities data with index in front for user to pick
    :param cities_data: An OrderedDictionary of cities data
    :return: None
    """
    for i, city in enumerate(cities_data):
        print(f"{i + 1} - {city}")


def turtle_city_projection(cities_data: OrderedDict) -> None:
    """
    Project all city projection in the next following years
    :param cities_data:
    :return: None
    """
    try:
        initial_population = int(input("Enter the starting population: "))
        assert initial_population >= 0
        number_of_years = int(input("Enter number of years: "))
        assert number_of_years > 0
        rate = float(input("Enter growth rate as a percentage (0.10): "))
        assert rate > 0
    except ValueError and AssertionError:
        print("Invalid Input. Must be natural number")

    # turtle initialize
    ninja = turtle.Turtle()
    screen = ninja.getscreen()
    screen.setup(600, 600)
    screen.title(f"Cities Projection")
    turtle.bgcolor("white")
    ninja.speed(0)
    scale = scale_factor(cities_data, number_of_years, rate)

    # drawing frame
    graph_goto = relative_goto(ninja, -250, -250)
    draw_frame(ninja, graph_goto)

    # draw graph text
    jump(ninja, 0, -270)
    ninja.write(f"Cities population projection ({number_of_years} years)",
                move=False, align="center",
                font=("comic sans", 12, "bold"))

    for city in cities_data:
        death, born, move_in, delta = cities_data[city]

        # draw graph
        ninja.speed(2)
        x_delta = 0
        y_delta = initial_population / Y_RATE
        jump(ninja, X_LENGTH / -2, Y_LENGTH / -2 + y_delta)
        pen_color = random.choice(["blue", "red", "purple",
                                   "green", "orange", "salmon", "brown"])
        ninja.pen(pencolor=pen_color, pensize=2)

        for year in range(number_of_years + 1):

            graph_goto(x_delta, y_delta * scale)

            # stamp
            ninja.dot(8)

            # write population
            ninja.penup()
            graph_goto(x_delta - 4, y_delta * scale + 6)
            ninja.write(f"{int(y_delta)}", align="center")
            graph_goto(x_delta, y_delta * scale)
            ninja.pendown()

            # calculation
            x_delta += X_LENGTH / number_of_years
            y_delta += delta
            y_delta *= (1 + rate)

    # hide turtle
    ninja.hideturtle()

    # exit
    turtle.exitonclick()


def turtle_main() -> None:
    print_welcome()
    cities_data = OrderedDict()
    try:
        cities_data = read_cities()
    except FileNotFoundError:
        sys.exit(1)

    if len(cities_data) == 0:
        print("No cities data")
        run = False
    else:
        print_cities_data(cities_data)

    turtle_city_projection(cities_data)


if __name__ == "__main__":
    turtle_main()
