from pprint import *
import sys


WELCOME_MSG = "Welcome to the Crossword Creator 2 by Yitian Huang" +\
              " and Charlie Taylor!"
WORD_PROMPT = "Enter a word between 2 to 7 characters: "
HINT_PROMPT = "Enter a hint to that word that's less than 100 characters: "
TOTAL_PROMPT = "How many words would you like to include? (4-9)"


class Coordinate:
    def __init__(self, r, c) -> None:
        self.r = r
        self.c = c

    def c_diff(self, other: "Coordinate"):
        return abs(self.c - other.c)
    
    def r_diff(self, other: "Coordinate"):
        return abs(self.r - other.r)


def make_grid(rows:int, columns:int) -> list:    
    ''' returns nested list/grid based on parameter dimensions '''    
    return [["-" for idx in range(columns)] for idx in range(rows)]


def place_word(grid: list,  letters: list, start: Coordinate, end: Coordinate):
    '''
    takes 2 Coordinates and places word into grid
    '''

    if len(letters) not in [(end.r - start.r) + 1, (end.c - start.c) + 1]:
        print("Word length does not match coordinates")
        sys.exit()

    vertical = end.r_diff(start) > end.c_diff(start)

    if vertical:
        startPos, endPos = start.r, end.r
    else:
        startPos, endPos = start.c, end.c

    for idx, pos in enumerate(range(startPos, endPos + 1)):
        if vertical:
            anchor = start.c
        else:
            anchor = start.r

        if vertical:
            place = grid[pos][anchor]
            if place == '-' or place == letters[idx]:
                grid[pos][anchor] = letters[idx]
            else:
                print("Invalid word placement, try again next time")
                sys.exit()
        else:
            place = grid[anchor][pos]
            if place == '-' or place == letters[idx]:
                grid[anchor][pos] = letters[idx]
            else:
                print("Invalid word placement, try again next time")
                sys.exit()


def format_grid(grid: list, words: dict):
    '''
    takes grid and replaces all letters with blanks and puts in numbers where
    words start
    '''
    for line in range(len(grid)):
        for cell in range(len(grid[line])):
            if grid[line][cell] != '-':
                grid[line][cell] = '_'
    
    for word in words:
        start = words[word][1][0]
        grid[start.r][start.c] = words[word][-1]
    
    return grid


def to_txt(grid: list, words: dict):
    '''
    generates text file from given input
    '''
    cross = open('yourpuzzle.txt', 'w')
    for line in grid:
        for cell in line:
            cross.write(str(cell) + ' ')
        cross.write('\n')
    
    cross.write("Hints:\n")
    cross.write("Vertical\n")
    for word in words.items():
        # if is vertical
        if word[1][2]:
            cross.write(str(word[1][-1])+ '. ' + word[1][0] + '\n')
    cross.write('\n')
    cross.write("Horizontal\n")
    for word in words.items():
        # if is horizontal
        if not word[1][2]:
            cross.write(str(word[1][-1])+ '. ' + word[1][0] + '\n')


    cross.write('\n')

    cross.close()


def display_grid(grid: list, words: dict):
    '''
    prints to_txt contents to the shell
    '''
    for line in grid:
        for cell in line:
            print(str(cell) + ' ', end="")
        print('\n')
    
    print("Hints:\n")
    print("Vertical\n")
    for word in words.items():
        # if is vertical
        if word[1][2]:
            print(str(word[1][-1])+ '. ' + word[1][0])
    print('\n')
    print("Horizontal\n")
    for word in words.items():
        # if is horizontal
        if not word[1][2]:
            print(str(word[1][-1])+ '. ' + word[1][0])
