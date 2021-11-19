
def getNames(name_list):
    fl = open('girl_names.txt', 'r')
    for i in fl:
        strg = i.strip('\n')
        name_list.append(strg)
    return name_list]\

def linear(name_list, x):
    for i in name_list:
        if x.upper == i:
            return(f"{x} loops to find {x}")
    return(f"{x} not found.")

def binary(name_list, x):
    l = 0
    r = len(name_list)
    while l <= r:
        m = l + ((r-1) // 2)
        res = (x == name_list[m])

        if res == 0:
            return m - 1

        if res > 0:
            l = m + 1 

        else:
            r = m - 1 

    return(f"")


    

def main(name_list, x, y):
    getNames(name_list)
    if y == "L":
        print(linear(name_list, x))
    elif y == "B":
        print(binary(name_list, x))


name_list = []
x = input("Enter the name to search for: ")
y = input("Linear (L) or Binary (B): ")

