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
        self.left = 1
        self.right = 0
        self.WHERE_TO_INSERT = self.left
        self.scope:List[Node] = []
        
    def isTreeEmpty(self):
        return self.root == None
    #it builds a tree
    def build(self,linearCode: Tuple):
        linearCode = list(str(linearCode))
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
                    bundle:Tuple[Node, Node, Node, int] = self.__extractInfoFromLeaf(linearCode[i:])
                    if (self.isTreeEmpty()):
                        self.root = bundle[0]
                        scope.append(self.root)
                    else:
                        if (self.WHERE_TO_INSERT == self.left):
                            scope[-1].left = bundle[0]
                        else:
                            scope[-1].right = bundle[0]
                            self.WHERE_TO_INSERT = self.left
                        scope.append(bundle[0])
                    scope[-1].left = bundle[1]
                    scope[-1].right = bundle[2]
                    scope.pop()
                    i = bundle[3]
                    continue
                        
            elif (currentSymboll == ')' and i != len(linearCode)-1):
                scope.pop()
            elif currentSymboll == ',' and linearCode[i+2] != '(':
                self.WHERE_TO_INSERT = self.right
            elif (currentSymboll >= '0' and linearCode[i] <= '9'):
                currentElem = Node(self.__getOperand(linearCode[i:]))
            elif (currentSymboll == "'"):
                currentElem = Node(self.__getOperator(linearCode[i+1]))

            if ((not self.root) and self.notTerminatorCharacter(self.root)):

                self.root = currentElem

                scope.append(self.root)
            elif (self.root and i != len(linearCode)-1) :
                if (self.WHERE_TO_INSERT == self.left):
                    scope[-1].self.left = currentElem
                else:
                    scope[-1].right = currentElem
                scope.append(currentElem)
            i+= 1
            
    def notTerminatorCharacter(self, char):
        return (not (char in [","  ,  "("  ,  ")"  ,  "'"]))
        
        
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
        currentIndex = linearCodeSlice.index(')');
        
        root:Node = Node(self.__getRootLeaf(linearCodeSlice))
        leftChild:Node = Node(self.__getLeftLeaf(linearCodeSlice))
        rightChild:Node = Node(self.__getRightLeaf(linearCodeSlice))


        return (root, leftChild, rightChild, currentIndex) 
    
    def __getRootLeaf(self,linearCodeSlice):
        """
        input: (<root>, <leftChild>, <rightChild>)
        """
        i = 0
        root:str = ""
        while (linearCodeSlice[i] != ','):
            currentChar = linearCodeSlice[i] 
            if ((currentChar != '(') and (currentChar != "'")):
                root+= currentChar
            i+=1
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
        while (linearCodeSlice[i] != ')'):
            rightLeaf += linearCodeSlice[i]
            i+=1
        return rightLeaf

myTree = Tree()
myTree.build(('+', ('expt', 'x', 2), ('expt', 'y', 2)))

print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
print("tudo certo")