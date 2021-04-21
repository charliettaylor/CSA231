from os import kill
from pprint import *

WELCOME_MSG = "Welcome to the Crossword Creator by Charlie Taylor!"
WORD_PROMPT = "Enter a word between 2 to 10 characters: "
HINT_PROMPT = "Enter a hint to that word that's less than 100 characters: "
TOTAL_PROMPT = "How many words would you like to include? (4-9)"
changeable_grid = list()


def welcome():
    print("-" * len(WELCOME_MSG))
    print(WELCOME_MSG)
    print("-" * len(WELCOME_MSG))


def make_grid(across:int, down:int) -> list:    
    ''' returns nested list/grid based on parameter dimensions '''    
    global changeable_grid    
    for each in range(across):        
        square = list()        
    for each in range(down):            
        square.append(['x'])        
    changeable_grid.append(square)    
    return changeable_grid


def get_input() -> list:
    words = {}
    totalWords = 0
    while totalWords > 9 or totalWords < 4:
        try:
            totalWords = int(input(TOTAL_PROMPT))
        except ValueError:
            print("Please enter a positive integer")
    
    while(len(words) < totalWords):
        word = input(WORD_PROMPT)
        while len(word) < 2 or len(word) > 10:
            word = input(WORD_PROMPT)

        hint = input(HINT_PROMPT)
        while len(hint) > 100 or len(hint) < 1:
            hint = input(WORD_PROMPT)

        words[word] = hint
    print('input: ', words)
    return words


def check_collisions(words: dict) -> list:
    '''
    returns list of words that have collisisons with other words in list
    '''
    letters = []
    for word in words.keys():
        letters.append(set(word))
    
    collisions = []
    for idx, word in enumerate(letters):
        for compare in letters:
            if not word.isdisjoint(compare) and word is not compare:
                collisions.append(list(words.keys())[idx])
                break

    print('collisions', collisions)
    return collisions

def clean_input(words: dict, collisions: list) -> dict:
    '''
    removes words that do not have collisions from words dict
    '''
    remove = []
    for word in words:
        if word not in collisions:
            remove.append(word)

    for thing in remove:
        del words[thing]
    
    return words


yeet = ['wow', 'ass', "charlie", "andrew", "zebro", "xxx"]
test = get_input()
pprint(clean_input(test , check_collisions(test)))