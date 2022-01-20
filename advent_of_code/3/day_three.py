
### Advent of Code --> Day Three: ###

"""

Two new binary num:
- gamma rate 
- epsilon rate

Parameter #1 --> power consump (gamma rate * epsilon rate)

"""

### Part One:

with open('day_three_data.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    binary_len = len(lines[0])
    data_len = len(lines)
    gamma_rate = ''
    epsilon_rate = ''
    index = 0

    while index < binary_len:
        count1 = 0
        for line in lines:
            if line[index] == '1':
                count1 += 1
        if count1 > data_len/2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
        index += 1

print(f'Power consumption: {int(gamma_rate, 2)*int(epsilon_rate, 2)}')

### Part Two: 

## bit criteria:

# oxygen generator rating:

with open('day_three_data.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def oxygen_bit_crit(lines):
    bin_crit_lst = lines
    
    binary_len = len(lines[0])
    data_len = len(lines)
    index = 0

    while index < binary_len and len(bin_crit_lst) != 1:
        count1 = 0
        for line in lines:
            if line[index] == '1':
                count1 += 1
        if count1 > data_len/2:
            bin_crit_lst = [value for value in bin_crit_lst if value[index] != '0']
        elif count1 == data_len/2:
            bin_crit_lst = [value for value in bin_crit_lst if value[index] != '0']
        else:
            bin_crit_lst = [value for value in bin_crit_lst if value[index] != '1']
        index += 1

    return bin_crit_lst

def CO2_bit_crit(lines):
    bin_crit_lst = lines
    
    binary_len = len(lines[0])
    data_len = len(lines)
    index = 0

    while index < binary_len and len(bin_crit_lst) != 1:
        count1 = 0
        for line in lines:
            if line[index] == '1':
                count1 += 1
        if count1 > data_len/2:
            bin_crit_lst = [value for value in bin_crit_lst if value[index] != '1']
        elif count1 == data_len/2:
            bin_crit_lst = [value for value in bin_crit_lst if value[index] != '1']
        else:
            bin_crit_lst = [value for value in bin_crit_lst if value[index] != '0']
        index += 1

    return bin_crit_lst

print(f'Life support rating: {int(oxygen_bit_crit(lines)[0], 2)*int(CO2_bit_crit(lines)[0], 2)}')






