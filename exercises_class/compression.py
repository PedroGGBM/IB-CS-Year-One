# Compression and decompression func - Pedro G

import re

def compress(string):

    string += ' ' # 
    compress = ''
    i = 0

    while string[i] != ' ':

        counter_x = 0
        counter_y = 0

        while string[i] == "X":
            counter_x += 1 # what will determine how many X's there are 
            i += 1

        while string[i] == "O":
            counter_y += 1 # what will determine how many O's there are 
            i += 1

        compress += f"{counter_x}O{counter_y}*"
    
    if compress[-2] == "0": # couldn't manage to get rid of the O0 at the end of a string without O's, this if else statement only works with strings where X and O's don't exceed 9 letters
        return compress[:-3]
    else:
        return compress[:-1]

def decompress(string):

    decompressed = ''
    de_comp = string.split("*")
    print()

    for i in range(0, len(de_comp)):
        int_values = (re.findall('\d+', de_comp[i])) # makes a list of all seperate values (int) in between str types (the O in between)
        decompressed += (int(int_values[0])*"X") + (int(int_values[1])*"O")

    return decompressed
        
def main():
    x = str(input("Would you like to compress (1) or decompress a string? Please enter 1 or 2: "))
    if x == "1":
        string = str(input("Enter a string of X's and O's: "))
        print("Compressed data: " + str(compress(string)))
        print(f"\nOriginal data has been reduced in size by {100-(len(compress(string))/len(string))*100:.0f}%")
    if x == "2":
        string = str(input("Enter a decompressed string of X's and O's: "))
        print("Decompressed data: " + decompress(string))

main()