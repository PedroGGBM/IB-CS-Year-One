
# Advent of Code --> Day Four:

import os, math
import numpy as np

def bingo():
    with open('day_four_data.txt') as file:
        lines = file.readlines()
        lst = [int(line.rstrip()) for line in lines]

        print(f'init bingo nums: {len(lst)}')

    bingo_matrix = [
        [],[],[],[],[],
        [],[],[],[],[],
        [],[],[],[],[],
        [],[],[],[],[],
        [],[],[],[],[]
    ]

    count1 = 0
    count2 = 0
    for i in range(len(bingo_matrix)):
        for j, n in enumerate(bingo_matrix):
            if bingo_matrix[i][n] in lst[0]:
                count1 += 1

bingo()

"""

#################################

"""