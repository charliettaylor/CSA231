# The Game of Pig by Charlie Taylor
import sys
import random as rand
import playsound as ps
# side 1, feet 2, back 3, snout 4, ears and nose 5, touching 6
DICE_BIAS = (0.30, 0.25, 0.15, 0.1, 0.1, 0.1)


def dice() -> int:
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


def doubles(rolls: list) -> int:
    '''
    checks rolled dice to see what kind of double has been thrown, returns the
    point value of the double or 0 if there is no double

    rolls: a list of length 2 that has the player's dice rolls
    '''
    assert rolls != 0
    assert len(rolls) == 2
    if rolls[0] == rolls[1]:
        ps.playsound("Pig_idle2.mp3")
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
            ps.playsound("you-died.mp3")
            return -2
    return 0
# assert doubles([6, 6]) == -2


def mixed_combo(score: int, rolls: list) -> int:
    '''
    matches roll to score and prints out a message based on that, returns score
    to be added to total player score
    '''
    scores = [0, 5, 5, 10, 15]
    messages = ['Sider', 'Trotter', 'Razorback', 'Snouter', 'Leaning Jowler']
    if rolls[0] == 6 or rolls[1] == 6:
        ps.playsound("Pig_death.mp3")
        print("You rolled an Oinker!")
        return -1 * score
    # scores[] is in order of what you can roll
    ps.playsound("pigman.mp3")
    print("Mixed Combo:", messages[rolls[0] - 1],
          "and", messages[rolls[1] - 1])
    return (scores[rolls[0] - 1]) + (scores[rolls[1] - 1])
# assert mixed_combo(10, [1, 2]) == 5


def game_loop(p1Name: str, p2Name: str, maxScore: int):
    '''
    main game loop that controls turns/score and asks for input from players

    :param p1Name: is retrieved from command line
    :param p2Name: is retrieved from command line
    :param maxScore: is retrieved from command line
    '''
    score1 = 0
    score2 = 0
    turn = 1
    p1Play = True
    p2Play = True
    user_input = ''
    # 0 == false
    while p1Play or p2Play:
        if turn == 1 and p1Play:
            p1Play = True
            print('-' * 25)
            user_input = input(p1Name + "'s turn, roll or pass? ")
            if user_input.lower() == 'roll':
                add = take_turn(score1)
                if add == -2:
                    p1Play = False
                    p2Play = False
                elif add <= 0:
                    score1 += add
                    turn = 1 - turn
                else:
                    score1 += add
                    print(p1Name, "score:", score1)
                    print(p2Name, "score:", score2)
            elif user_input.lower() == 'pass':
                print(p1Name, 'has passed to', p2Name)
                turn = 1 - turn
        elif turn == 0 and p2Play:
            p2Play = True
            print('-' * 25)
            user_input = input(p2Name + "'s turn, roll or pass? ")
            if user_input.lower() == 'roll':
                add = take_turn(score2)
                if add == -2:
                    p2Play = False
                    p1Play = False
                elif add <= 0:
                    score2 += add
                    turn = 1 - turn
                else:
                    score2 += add
                    print(p1Name, "score:", score1)
                    print(p2Name, "score:", score2)
            elif user_input.lower() == 'pass':
                print(p2Name, 'has passed to', p1Name)
                turn = 1 - turn
        if score1 >= maxScore or score2 >= maxScore:

            print(p1Name if score1 >= maxScore else p2Name, "has won!")
            p1Play = False
            p2Play = False
    print("------------")
    print("Final scores")
    print("------------")
    print(p1Name, "scored:", score1)
    print(p2Name, "scored:", score2)


def take_turn(score: int) -> int:
    '''
    takes in a player score and returns the amount of points made in a turn
    '''
    turn = [dice(), dice()]
    doubleCheck = doubles(turn)
    if doubleCheck != 0:
        return doubleCheck
    elif doubleCheck == 0:
        return mixed_combo(score, turn)


def main():
    '''
    retrieves command line arguments and checks score, then runs game loop
    '''
    p1Name = sys.argv[1]
    p2Name = sys.argv[2]
    try:
        maxScore = int(sys.argv[3])
    except ValueError:
        print("Input for max score must be a number!")
    game_loop(p1Name, p2Name, maxScore)


if __name__ == "__main__":
    main()
