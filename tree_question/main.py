 
import math, random, os
 
class Node:
    def __init__(self, question, value):
        self.noNode = None
        self.yesNode = None
        self.qts = question
        self.val = value
       
 
class binaryTree:
    def __init__(self):
        self.root = None
       
    def getRoot(self):
        return self.root
 
    def add(self, question, value):
        if self.root is None:
            self.root = Node(question, value)
        else:
            self.__add(question, value, self.root)
 
    def __add(self, question, value, node):
        if value == 'no':
            if node.noNode is not None:
                self.__add(question, value, node.noNode)
            else:
                node.noNode = Node(question, value)
 
        else:
            if node.yesNode is not None:
                self.__add(question, value, node.yesNode)
            else:
                node.yesNode = Node(question, value)
 
    def printTree(self):
        entries = []
        if self.root is not None:
            # recursive call to grab last leaf (not child)
            entry = self.__printTree(self.root)
            entries.append(entry)
        return entries # meant to
       
   
    def __printTree(self, node):
        entries = []
        if node is not None:
            self.__printTree(node.noNode)
            return(f'{str(node.qts)};{str(node.val)}')
            self.__printTree(node.yesNode)
 
    def deleteTree(self):
        self.root = None
 
def startNewGame(binaryTree):
    global root
    # create binary tree instance
    root = binaryTree()
   
    # welcome
    print('Welcome to the object guessing game!\n\nThink of an object to train')
 
    # first node
    x = str(input('Please input a question that would distinguish your object: '))
   
    # incorrect value input
    noVal = str(input('Input an object that would disatisfy the question: '))
    root.add(x, noVal)
 
    # correct value input
    yesVal = str(input('Input an object that would satisfy the question: '))
    root.add(x, yesVal)
 
def playGame(root):
    global final
    global qts_final
    global endgame
    # semi psuedocode
    while root.children is not None: # will print if leaf, no node children
        x = str(input(f"{root.qts}; write yes or no ")).lower()
        if x == "yes":
            root.yesNode # not correct, refers to moving to next node (righ)
        else:
            root.noNode # not correct ...
 
    x = str(input(f"Is your object a {root.qts}"))
    if x == 'yes':
        print("Computer won!")
    else:
        final = str(input(f"You win! What where you thinking of? "))
        qts_final = str(input("Please enter a question to distinguish a {final} from {root.qts}"))
    endgame = str(input("Would you like to play again? Type yes of no: ")).lower()
 
def updateGame(): # updates the nodes (adds last object question)
    if endgame == 'yes':
        root.add(qts_final, final)
        return 1
    else:
        root.deleteTree()
        return 0
 
def main(binaryTree):
    x = 1
    startNewGame(binaryTree)
    while x == 1: # flag to continue playing and updating the game
        playGame(root)
        updateGame()
    print("Thank you for playing, play again soon!")
 
if __name__ == '__main__':
    main(binaryTree)
 
"""
 
def startNewGame():
 
def playGame():
    at the end: updateGame()
 
def updateGame():
 
def main():
    startNewGame()
    playGame()
    updateGame()
 
----------------------------------------------------------------
 
initialize parent node question:
x = str(input('Please input a question that would distinguish your object: '))
y = str(input('Input an object that would disatisfy the question'))
z = str(input('Input an oject that would satisfy the question'))
 
"""
 
 

