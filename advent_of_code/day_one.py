
# with open('day_one_data.txt', 'r') as a_file:


#     count = 0
    
#     counter = 0
    
#     for line in a_file:

#         stripped_line = int(line.strip())
#         if stripped_line > counter:
#             count += 1

#         counter = int(stripped_line)

# print(count)

# second part

with open('day_one_data.txt') as file:
    lines = file.readlines()
    lst = [int(line.rstrip()) for line in lines]

print(lst)

count = 0

for i in range(len(lst)):
    if i >= 1 and i < len(lst)-2:
        if lst[i-1]+lst[i]+lst[i+1] > lst[i]+lst[i+1]+lst[i+2]:
            count += 1

print(count)