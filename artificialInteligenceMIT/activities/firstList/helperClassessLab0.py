from typing import List, Tuple

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def isOperator(self):
        operators = ['+', '-', '*', '/', 'expt']
        return self.value in operators
    def isOperand(self):
        return (not self.isOperator())

class Tree:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    #it builds a tree
    def build(self,linearCode: Tuple):
        left = 1
        right = 0
        WHERE_TO_INSERT = left
        linearCode = (str(linearCode))
        scope:List[Node] = []
        currentElem = None
        i = 0
        while (i < len(linearCode)):
            """
            when we got to this point. It it needed to know whether or
            not we are dealing with a leaf
            """
            currentSymboll = linearCode[i]
            if currentSymboll == '(':
                if (self.__isLeaf(linearCode[i+1:])):
                    bundle:Tuple[Node, Node, Node, int] = self.__extractInfoFromLeaf(linearCode[i])
                    if (self.isEmpty()):
                        self.root = bundle[0]
                        scope.append(self.root)
                    else:
                        if (WHERE_TO_INSERT == left):
                            scope[-1].left = bundle[0]
                        else:
                            scope[-1].right = bundle[0]
                            WHERE_TO_INSERT = left
                        scope.append(bundle[0])
                    scope[-1].left = bundle[1]
                    scope[-1].right = bundle[0]
                    scope.pop()
                    i = bundle[2]
                    continue
                        
            elif currentSymboll == ')':
                scope.pop()
            elif currentSymboll == ',' and linearCode[i+2] != '(':
                WHERE_TO_INSERT = right
            elif (currentSymboll >= '0' and linearCode[i] <= '9'):
                currentElem = Node(self.getOperand(linearCode[i:]))
            elif (currentSymboll == "'"):
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
            i+= 1
    def __getOperator(self,linearCodeSlice:str):
        """
        After converting the tuple to a string, you will have something like that
        <<('expt', 'b', 2)>> so it is needed to extract this "expt" in quotes, that's
        when this methods comes in.
        """
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
            if linearCodeSlice[i] == ')':
                return not parethesisAfterComma
            elif linearCodeSlice[i] == ',' and linearCodeSlice[i+2] == '(':
                return parethesisAfterComma
    def __extractLeaf(self, begginingIndex, linearCode:str):
        """
        It will take the whole linearCode along with the index of where the leaf in question
        starts and, based on that, it will extract the leaf.
        """
    def __extractInfoFromLeaf(self, linearCodeSlice:str) -> Tuple[Node, Node, Node, int]:
        """
        -format of a leaf: (<root>, <leftChild>, <rightChild>)
        -everything between the opening parethesis and the first comma is the root
        -everything between the first comma and the second one if the left child
        -everything between the second comma and the closing parethesis is the right child
        -for updating the index you just need to find the index of the closing parenthesis
        """
        root:Node = Node(self.__getRootOfLeaf(linearCodeSlice))
        leftChild:Node = Node(self.__getLeftLeaf(linearCodeSlice))
        rightChild:Node = Node(self.__getRightLeaf(linearCodeSlice))

        currentIndex = linearCodeSlice.index('(');

        return (root, leftChild, rightChild, currentIndex) 
    
    def __getRootLeaf(self,linearCodeSlice):
        """
        input: (<root>, <leftChild>, <rightChild>)
        """
        i = 0
        root:str = ""
        while (linearCodeSlice[i] != ','):
            if (linearCodeSlice[i] != '('):
                root+= linearCodeSlice[i]
        #updates the string
        del linearCodeSlice[:linearCodeSlice.index(',')+2]
        return root
    
    def __getLeftLeaf(self, linearCodeSlice):
        """
        <leftChild>, <rightChild>)
        """
        return self.__getRootLeaf(linearCodeSlice) #it works just the same
    
    def __getRightLeaf(self, linearCodeSlice):
        """
        <rightChild>)
        """
        rightLeaf: str = ""
        i = 0
        while (linearCodeSlice[i] != '('):
            rightLeaf += linearCodeSlice[i]
        return rightLeaf

myTree = Tree()
myTree.build((('expt', 'x', 2)))
print("tudo certo")