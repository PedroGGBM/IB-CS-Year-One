
def getNames(name_list):
    load = open("C:/Users/Pedro Gronda/Desktop/Python3.8/IB_CS/compsci_search_sort/random_words.txt",'r')
    for i in load:
        string = i.strip('\n')
        name_list.append(string)
    return name_list

def selectionSort(name_list, n):
    for i in range(len(name_list)):
        index = i
        for j in range(i+1, len(name_list)):
            n += 1
            if name_list[index] > name_list[j]:
                index = j
        name_list[i], name_list[index] = name_list[index], name_list[i]
    return n

def bubbleSort(name_list, l):
    for i in range(len(name_list)):
        for j in range(0, len(name_list)-i-1):
            l += 1
            if name_list[j] > name_list[j+1]:
                name_list[j], name_list[j+1] = name_list[j+1], name_list[j]

if __name__ == '__main__':
    name_list = []
    n = 0
    l = 0
    name_list = getNames(name_list)
    n = selectionSort(name_list, n)
    name_list = getNames(name_list)
    l = bubbleSort(name_list, l)
    print(f"Selection sort took {n} loops to sort the list (worst case O(n^2) = 22500)")
    print(f'Bubble sort took {l} loops to sort the list (worst case O(n^2) = 22500)')