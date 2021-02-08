# The Game of Pig by Charlie Taylor

import random as rand
# side 1, feet 2, back 3, snout 4, ears and nose 5, touching 6
DICE_BIAS = (0.35, 0.3, 0.2, 0.1, 0.04, 0.01)


def dice():
    '''
    rolls weighted 'dice' that represent each part of the pig and returns an
    integer
    '''
    roll = rand.random()
    sum = 0
    result = 1
    for mass in DICE_BIAS:
        sum += mass
        if roll < sum:
            return result
        result += 1


def doubles(rolls: list):
    '''
    checks rolled dice to see what kind of double has been thrown, returns the
    point value of the double or 0 if there is no double
    '''
    if rolls[0] == rolls[1]:
        if rolls[0] == 1:
            print("You rolled a Double Sider")
            return 1
        elif rolls[0] == 2:
            print("You rolled a Double Trotter")
            return 20
        elif rolls[0] == 3:
            print("You rolled a Double Razorback")
            return 20
        elif rolls[0] == 4:
            print("You rolled a Double Snouter")
            return 40
        elif rolls[0] == 5:
            print("You rolled a Double Leaning Jowler")
            return 60
        elif rolls[0] == 6:
            print("You rolled a Piggyback")
            return -2
    return 0


def mixed_combo(score: int, rolls: list):
    '''
    matches roll to score and prints out a message based on that, returns score
    to be added to total player score
    '''
    scores = [0, 5, 5, 10, 15]
    messages = ['Sider', 'Trotter', 'Razorback', 'Snouter', 'Leaning Jowler']
    if rolls[0] == 6 or rolls[1] == 6:
        print("You rolled an Oinker!")
        return -1 * score
    # scores[] is in order of what you can roll
    print("Mixed Combo:", messages[rolls[0] - 1],
          "and", messages[rolls[1] - 1])
    return (scores[rolls[0] - 1]) + (scores[rolls[1] - 1])


def game_loop(p1Name: str, p2Name: str, maxScore: int):
    '''
    continues looping turns until someone wins
    '''
    score1 = 0
    score2 = 0
    turn = 1
    p1Play = True
    p2Play = True
    user_input = ''
    # 0 == false
    while p1Play or p2Play:
        if turn and p1Play:
            print('-' * 25)
            user_input = input(p1Name + "'s turn, roll or pass? ")
            if user_input.lower() == 'roll':
                add = take_turn(score1)
                if add == -2:
                    p1Play = False
                else:
                    score1 += add
                    print(p1Name, "score:", score1)
                    print(p2Name, "score:", score2)
            elif user_input.lower() == 'pass':
                print(p1Name, 'has passed to', p2Name)
                turn = 1 - turn
            if score1 >= maxScore:
                print(p1Name, "has won!")
                p1Play = False
                p2Play = False
        elif p2Play:
            print('-' * 25)
            user_input = input(p2Name + "'s turn, roll or pass? ")
            if user_input.lower() == 'roll':
                add = take_turn(score2)
                if add == -2:
                    p2Play = False
                else:
                    score2 += add
                    print(p1Name, "score:", score1)
                    print(p2Name, "score:", score2)
            elif user_input.lower() == 'pass':
                print(p2Name, 'has passed to', p1Name)
                turn = 1 - turn
            if score1 >= maxScore:
                print(p2Name, "has won!")
                p1Play = False
                p2Play = False
    print("Final scores")
    print(p1Name, "scored", score1)
    print(p2Name, "scored", score2)


def take_turn(score: int) -> int:
    '''
    takes in a player variable of either 1 or 0 and returns a score
    '''
    turn = [dice(), dice()]
    doubleCheck = doubles(turn)
    if doubleCheck != 0:
        return doubleCheck
    elif doubleCheck == 0:
        return mixed_combo(score, turn)


def main():
    p1Name = input("Enter player 1's name: ")
    p2Name = input("Enter player 2's name: ")
    maxScore = int(input("Enter a score to play to: "))
    while int(maxScore) <= 0:
        maxScore = int(input("Please enter a score greater than 0: "))
    game_loop(p1Name, p2Name, maxScore)


if __name__ == "__main__":
    main()
