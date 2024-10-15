from typing import *

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def isOperator(self):
        operators = ['+', '-', '*', '/', 'expt']
        return self.value in operators
    def isOperand(self):
        return (not isOperator)

class Tree:
    def __init__(self):
        self.root = None

    def __init__(self, value):
        self.root = Node(value)
    
    #it builds a tree
    def build(linearCode: Tuple):
        left = 1
        right = 0
        WHERE_TO_INSERT = left
        linearCode = (str(linearCode))
        scope:List[Node] = []
        currentElem = None
        for i in range(len(linearCode)):
            """
            when we got to this point. It it needed to know whether or
            not we are dealing with a leaf
            """
            if linearCode[i] == '(':
                if (self.__isLeaf(linearCode[i+1:])):
                    pass

            elif linearCode[i] == ')':
                scope.pop()
            elif linearCode[i] == ',' and linearCode[i+2] != '(':
                WHERE_TO_INSERT = right
            elif (linearCode[i] >= '0' and linearCode[i] <= '9'):
                currentElem = Node(self.getOperand(linearCode[i:]))
            elif (linearCode[i] == "'"):
                currentElem = Node(self.getOperator(linearCode[i+1]))

            if (not self.root):
                self.root = currentElem
                scope.append(self.root)
            else :
                if (WHERE_TO_INSERT == left):
                    scope[-1].left = currentElem
                else:
                    scope[-1].right = currentElem
                scope.append(currentElem)
    """
    After converting the tuple to a string, you will have something like that
    <<('expt', 'b', 2)>> so it is needed to extract this "expt" in quotes, that's
    when this methods comes in.
    """
    def __getOperator(self,linearCodeSlice:str):
        value: str = ""
        for i in range(len(linearCodeSlice)):
            if (linearCodeSlice[i] == "'"):
                break
            value += linearCodeSlice[i]
        return value
    def __getOperand(self,linearCodeSlice:str):
        value: str = ""
        for i in range(len(linearCodeSlice)):
            if (linearCodeSlice[i] == ',' or linearCodeSlice[i] == ')'):
                break
            value += linearCodeSlice[i]
        return value
    def __isLeaf(self, linearCodeSlice:str):
        parethesisAfterComma:bool = False
        for i in range(len(linearCodeSlice)):
            if linearCodeSlice[i] == ',' and linearCodeSlice[i+2] == '(':
                return parethesisAfterComma
        return not parethesisAfterComma 
    def __extractChildren(self, linearCodeSlice:str):
        leftChild:str = ""
        rightChild:str = ""
        isFirst:bool = True
        for i in range(len(linearCodeSlice)):
            if (line)