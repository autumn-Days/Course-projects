from typing import *

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def isOperator():
        operators = ['+', '-', '*', '/', 'expt']
        return self.value in operators
    def isOperand:
        return (not isOperator)

class Tree:
    def __init__(self):
        self.root = None

    def __init__(self, value):
        self.root = Node(value)
    
    #it builds a tree
    def build(linearCode: Tuple):
        left = 0
        right = 1
        WHERE_TO_INSERT = left
        linearCode = (str(linearCode))
        previous:List[Node] = []
        currentOperand = None
        for i in range(len(linearCode)):
            #We can totally disconsider the left parenthesis
            if linearCode[i] == '(':
                continue
            elif (linearCode[i] >= '0' and linearCode[i] <= '9'):
                currentOperand = self.getOperand(linearCode[i:])
            if (self.root == None):
                self.root = Node(self.getValue(linearCode[i+1:]))
                previous.append(self.root)
    """
    After converting the tuple to a string, you will have something like that
    <<('expt', 'b', 2)>> so it is needed to extract this "expt" in quotes, that's
    when this methods comes in.
    """
    def getOperator(linearCodeSlice:str):
        value: str = ""
        for i in range(len(linearCodeSlice)):
            if (linearCodeSlice[i] == "'"):
                break
            value += linearCodeSlice[i]
        return value
    def getOperand(linearCodeSlice:str):
        pass