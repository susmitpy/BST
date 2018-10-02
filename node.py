class Node:
    def __init__(self, value):
        self.value = value
        self.LeftChild = None
        self.RightChild = None
        self.Parent = None

    def hasLeftChild(self):
        if self.LeftChild:
            return True
        return False

    def hasRightChild(self):
        if self.RightChild:
            return True
        return False

    def getParent(self):
        return self.Parent

    def getLeftChild(self):
        if not isinstance(self, node):
            return " "
        if self.hasLeftChild:
            return self.LeftChild
        return " "

    def getRightChild(self):
        if not isinstance(self, node):
            return " "
        if self.hasRightChild:
            return self.RightChild
        return " "