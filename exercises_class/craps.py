
# craps game - Pedro G

import random

"""the function do_roll() will "roll" and add the sum of both dice"""
def roll():
    dice_num1=random.randint(1, 6)
    dice_num2=random.randint(1, 6)
    print(f"Computer rolls a {dice_num1} and a {dice_num2}, for a total of {dice_num1+dice_num2}.")
    return dice_num1 + dice_num2

def process():
    x = roll()
    while x != [7, 11]:
        

    print('You lose :/')

point = 0
# """This while statement is for until the value point is in the number range 4, 5, 6, 8, 9, 10"""
while point not in [4, 5, 6, 8, 9, 10]: 
    point = do_roll() #while it isn't in the previous number range, roll again
print(f"{point} is now the established POINT.")

total_score = 0
# """This while statement is for setting the variable total_score to the sum of dice, with the condition that it will stop when it is either point or the num 7"""
while total_score not in [point, 7]: 
    total_score = do_roll()
if total_score == 7:
    print('YOU LOSE')
else:
    print('YOU WIN')
