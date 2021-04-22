from cross1 import *

changeable_grid = list()

def welcome():
    print("-" * len(WELCOME_MSG))
    print(WELCOME_MSG)
    print("-" * len(WELCOME_MSG))


def get_input() -> list:
    words = {}
    totalWords = 0
    rows = int(input("How many rows do you want? "))
    cols = int(input("How many columns do you want? "))

    while totalWords > 9 or totalWords < 4:
        try:
            totalWords = int(input(TOTAL_PROMPT))
        except ValueError:
            print("Please enter a positive integer")
    
    vert_count = 1
    horiz_count = 1
    while(len(words) < totalWords):
        word = input(WORD_PROMPT)
        while len(word) < 2 or len(word) > 8:
            word = input(WORD_PROMPT)

        hint = input(HINT_PROMPT)
        while len(hint) > 100 or len(hint) < 1:
            hint = input(WORD_PROMPT)

        coords, is_vertical = coordinate_input(rows, cols)

        hint_number = None
        for k, v in words.items():
            if coords == v[1][0]:
                print("Same starting coordinate is not allowed")
                sys.exit(1)
        if is_vertical:
            hint_number = vert_count
            vert_count += 1
        else:
            hint_number = horiz_count
            horiz_count += 1
        
        words[word] = (hint, coords, is_vertical, hint_number)
    return [words, rows, cols]


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
    
    return word


def coordinate_input(rows: int, cols: int) -> list[Coordinate]:
    '''
    ask user for coordinate to input the word
    '''
    try:
        r1 = int(input("Enter start row: "))
        c1 = int(input("Enter start column: "))
        r2 = int(input("Enter end row: "))
        c2 = int(input("Enter end column: "))
        assert 0 <= r1 < rows
        assert 0 <= c1 < cols
        assert 0 <= r2 < rows
        assert 0 <= c2 < cols
    except (ValueError, AssertionError):
        print("Invalid coordinate input")
        sys.exit(1)
    
    start_coordinate = Coordinate(r1, c1)
    end_coordinate = Coordinate(r2,  c2)
    
    try:
        if r1 == r2: # vertical
            is_vertical = True
            assert c2 > c1
        else: # horizontal
            is_vertical = False
            assert r2 > r1
    except AssertionError:
        print("Invalid input")
        sys.exit(1)

        
    
    return (start_coordinate, end_coordinate), is_vertical

test = {
    'yee':['djdjdjdjdjd', (Coordinate(0,0), Coordinate(2,0)), True, 1],
    'oww':['pppppppd', (Coordinate(0,1), Coordinate(2,1)), True, 2],
    'bone':['dyyyyyyydjdjd', (Coordinate(0,2), Coordinate(3,2)), True, 3],
    'oof':['dkkkkkkkdjd', (Coordinate(0,3), Coordinate(2,3)), True, 4],
    'ewoo':['horiz', (Coordinate(1,0), Coordinate(1,3)), False, 1]
    }

def main():
    global changeable_grid
    welcome()
    words, rows, cols = test, 20, 20
    print("Thanks! We're making your crossword now...")
    changeable_grid = make_grid(rows, cols)
    
    for word in words:
        place_word(changeable_grid, word, words[word][1][0], words[word][1][1])
    
    changeable_grid = format_grid(changeable_grid, words)
    display_grid(changeable_grid, words)
    to_txt(changeable_grid, words)
    print("...done!")


def test_():
    main(test)


if __name__ == "__main__":
    main()
