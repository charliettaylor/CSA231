# The Game of Pig by Charlie Taylor

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

def dice():
    '''
    rolls weighted 'dice' that represent each part of the pig and returns an
    integer
    '''
    pass

def doubles():
    '''
    checks rolled dice to see what kind of double has been thrown, returns the
    point value of the double or 0 if there is no double
    '''
    pass

