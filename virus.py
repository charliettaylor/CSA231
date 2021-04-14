# viruses by Charlie Taylor

from turtle import *
import random as rand


def move_random(t: Turtle) -> None:
    '''
    moves given turtle to a random position without drawing
    '''
    t.up()
    x = rand.randint(-400, 400)
    y = rand.randint(-400, 400)
    t.goto(x, y)
    t.down()


def virus(t: Turtle, a, b, color) -> None:
    '''
    draws the virus based on given parameters
    :param t: turtle being used
    :param a: length of lines being drawn
    :param b: angle by which line is drawn
    :param color: str of what color to draw with
    '''
    t.pencolor(color)
    while True:
        t.fd(a)
        t.right(b)
        a += 2
        b += 1
        if b == 200:
            break


def main():
    wn = Screen()
    wn.bgcolor("black")
    wn.title("Turtle")
    t = Turtle()
    t.speed(0)

    colors = ["green", "orange", "salmon", "yellow"]
    for iter in range(5):
        length = 0
        angle = 0

        virus(t, length, angle, colors[rand.randint(0,len(colors) - 1)])
        move_random(t)


if __name__ == "__main__":
    main()
