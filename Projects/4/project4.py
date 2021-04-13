# Turtle Project by Charlie Taylor

from turtle import *
import random as rand

SCALE = "Enter the size of the spiral (recommend 1-10): "
LOW = "Enter low bound of shake (rec. negative or 0): "
HIGH = "Enter high bound of shake (rec. positive or 0): "


def draw_c(t) -> None:
    '''
    draws letter C
    '''
    t.down()
    for i in range(2):
        t.fd(100)
        t.left(90)
    t.fd(100)
    t.up()


def draw_t(t) -> None:
    '''
    draws letter T
    '''
    t.down()
    t.fd(100)
    t.left(90)
    t.fd(75)
    t.back(150)
    t.up()


def initials(t: Turtle) -> None:
    '''
    draws initials from any starting position
    '''
    t.setheading(180)
    draw_c(t)
    t.fd(100)
    t.left(90)
    draw_t(t)


def shake(low, high) -> int:
    '''
    returns an int to modify the degrees in spiral
    should be a negative number for low and positive for high to make effect
    look good
    '''
    return rand.randint(low, high)


def spiral(t, degrees, n, scale, low=0, high=0) -> None:
    '''
    Draws a spiral based on degrees and number of iterations entered

    t : Turtle object
    degrees : should be 1 less than interior angle of regular polygon
    n : number of iterations

    Keyword arguments
    low : lower bound of shake that varies degrees
    high : upper bound of shake that varies degrees
    '''
    size = 2
    t.down()
    for i in range(n):
        t.fd(size)
        t.left(degrees + shake(low, high))
        size += scale
    t.up()


def main():
    print("Welcome to the spiral maker by Charlie Taylor")
    done = False
    while not done:
        try:
            scale = float(input(SCALE))
            low = int(input(LOW))
            high = int(input(HIGH))
            done = True
        except ValueError:
            print("Enter a positive non zero integer")

    wn = Screen()
    wn.bgcolor("black")
    wn.title("Turtle")
    t = Turtle()
    t.speed(0)

    t.setposition(0, 0)
    t.pencolor("green")
    spiral(t, 119, 300, scale, low, high)

    t.pencolor("salmon")
    t.setposition(0, 0)
    spiral(t, 89, 300, scale, low, high)

    t.pencolor("orange")
    t.setposition(0, 0)
    spiral(t, 71, 300, scale, low, high)

    t.pencolor('white')
    t.setposition(0, 0)
    initials(t)

if __name__ == "__main__":
    main()
