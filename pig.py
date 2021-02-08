# The Game of Pig by Charlie Taylor

import random as rand

'''
1. Double Sider - The pigs are both on their sides - 1 Point
2. Double Razorback - The pigs are both lying on their backs - 20 Points
3. Double Trotter - The pigs are both standing upright - 20 Points
4. Double Snouter - The pigs are both leaning on their snouts - 40 Points
5. Double Leaning Jowler - The pigs are both resting between snouts and ears - 60 Points
6. Oinker - If both pigs are touching in any way, then the player's total score
 is reset to 0 and the turn changes to the next player.
7. Piggyback - If one pig lands completely resting on top of the other, then the
 player is out of the game. (According to the scoring rules on the front of the
  game package such a result is impossible, but it may very well happen in your game!
   - and your weighted random must consider this unlikely outcome).
8. Mixed Combo - A combination not mentioned above is the sum of the single pigs' scores.
 So if this outcome results from the roll, the following must be displayed
  (e.g. Mixed Combo: Sider and Leaning Jowler).
'''

'''
Your program should take the players' names and the target score as command line arguments, in that order.
When one player earns at least the target score, the game ends and that player wins.
The players should have the option to ROLL or PASS. Your program should be not be case sensitive; the user should be able to enter "ROLL" or "roll" or "Roll" or such thing.
If the player rolls, your program should randomly generate the pigs' landing positions and print out the result of the roll and how many points the player earned for that roll.
If the player rolls an Oinker, then the player loses ALL of his/her points, and play goes to the next player.
If the player rolls a Piggyback, the game ends and the other player wins!
Name your file pig.py
'''

# side 1, feet 2, back 3, snout 4, ears and nose 5, touching 6
DICE_BIAS = (0.35, 0.3, 0.2, 0.1, 0.04, 0.01)

def dice():
    '''
    rolls weighted 'dice' that represent each part of the pig and returns an
    integer
    '''
    roll = rand.random() # in [0,1]
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

# side 1, feet 2, back 3, snout 4, ears and nose 5, piggyback 6
def mixed_combo(score: int, rolls: list):
    scores = [0, 5, 5, 10, 15]
    messages = ['Sider', 'Trotter', 'Razorback', 'Snouter', 'Leaning Jowler']
    if rolls[0] == 6 or rolls[1] == 6:
        print("You rolled an Oinker!")
        return -1 * score
    #scores[] is in order of what you can roll
    print("Mixed Combo:", messages[rolls[0] - 1], "and", messages[rolls[1] - 1])
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
            user_input = input(p2Name +"'s turn, roll or pass? ")
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
    if doubleCheck != 0 and doubleCheck != -1:
        return doubleCheck
    elif doubleCheck == -1:
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
