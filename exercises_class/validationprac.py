
# values = [11, 12, 15, 16, 112, 118, 123, 145]
# target = 15
# minim = 0
# high = 7
# found = False
# answer = 0
# mid = 0

# while found != True and minim <= high:
#     mid = (minim+high)//2
#     if values[mid] == target:
#         found = True
#         answer = mid 
#     elif target > values[mid]:
#         minim = mid+1
#     else:
#         high = mid-1

# if found == True:
#     print(f"{target} found at array index {answer}")
# else:
#     print(f"{target} was not found")

def invert_byte(a_byte):
    for i in a_byte:
        if i == 1:
            a_byte[i] = 0
    return ''.join(a_byte)

a_byte = [1,0,0,0,1,1,0]
byte = invert_byte(a_byte) 
print(byte)   
