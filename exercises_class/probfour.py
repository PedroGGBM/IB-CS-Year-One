# import random

# while True:
#     n = int(input("Enter a number: "))
#     if n < 0:
#         raise ValueError
#     else:
#         for i in range(1, n+1):
#             if n % i == 0:
#                 print(i, end=" ")

# Continue = True
# while Continue:
#     num1 = random.randrange(1,9)
#     num2 = random.randrange(1,9)
#     product = num1 * num2
#     n = int(input(f"What is the product of {num1} and {num2} ? "))
#     if product == n:
#         print("Correct!") 
#     if product != n:
#         print("Not quite...")
#     if n < 0:
#         print("Goodbye for now.")
#         Continue = False


# names = ["Alma", "Betty", "Cora", "Dora", "Ella"]
# N = 5
# K = 0

# print(names)

# while (K < N - 1):
#     temp = names[K]
#     names[K] = names[N - K - 1]
#     names[N-K-1] = temp
#     K += 1
# print(names)

# n = 139
# l = 3

# d = n // l
# z = 1
# b = False

# print(f"{d:20}{z:10}{b:10}{z<l:10}")

# while z < l:
#     d = d // l
#     print(d, end="")
#     z += 1
#     print(z, end="")
#     b = not b
#     print(b, end="")
#     print("\n")

# if d != 0 and b:
#     print(b, d)
# else:
#     print(z, not b)

# mydata = [2, 4, -1, 3]

# for i in range(0, len(mydata)):
#     print(mydata[i])


# x = int(input("Enter a numkber of terms: "))
# for i in range(0, x):
#     print(2)

def main():
    namesList = []
    nameLength = 0
    cont = False
    while cont == False:
        x = str(input("Please enter a name: "))
        namesList.append(x)
        y = str(input("Do you wish to continue? Please write yes or no: "))
        if y == "no":
            cont = True
    print(namesList)
    for i in range(0, len(namesList)+1):
        temp1 = namesList[i]
        temp2 = namesList[i+1]
        if len(temp2) > len(temp1):
            name = temp2 
    print(f"{name} is the longest name in the list.")

main()