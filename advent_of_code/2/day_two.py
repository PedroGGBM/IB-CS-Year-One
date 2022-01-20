
# Advent of Code --> Day Two:

import re

with open('day_two_data.txt') as file:
    lst = file.readlines()
    
hor_pos = 0
ver_pos = 0
aim = 0

for i in range(len(lst)):
    if lst[i][0] == 'f':
        hor_pos += int(re.findall('\d+', lst[i])[0])
        ver_pos += aim*int(re.findall('\d+', lst[i])[0])
    if lst[i][0] == 'd':
        aim += int(re.findall('\d+', lst[i])[0])
    if lst[i][0] == 'u':
        aim -= int(re.findall('\d+', lst[i])[0])

print(hor_pos*ver_pos)





