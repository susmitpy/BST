class node:
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
        if self.hasLeftChild:
            return self.LeftChild
        return False

    def getRightChild(self):
        if self.hasRightChild:
            return self.RightChild
        return False

class BST:
    def __init__ (self):
        self.level = 0
        self.nodes = 0
        self.levels = []
 

    def Assign(self, value, current_node = None):
##        print("Assign is Called")
        if isinstance(value, list):
            for i in range(len(value)):
                self.Assign(value[i])
        else:
            if not self.nodes:
    ##            print("Creating Root Node")
                self.root_node = node(value)
                self.curr_node = node(value)
                self.Increament()
            else:
                if not current_node:
                    self.curr_node = self.root_node
    ##            print("Comparing {} and {}".format(self.curr_node.value, value))
                self.Compare(self.curr_node.value, value)

    def Compare(self, P, TC):       
        if self.nodes != 0:           
            if P < TC:
##                print("{} < {}".format(P, TC))
##                print("Going Right")
                self.GoRight(TC)                
            else:
##                print("{} > {}".format(P, TC))
##                print("Going Left")
                self.GoLeft(TC)

    def GoLeft(self, TC):        
        if not self.curr_node.LeftChild:
##            print("Creating LC")
            self.curr_node.LeftChild = node(TC)
            self.curr_node.LeftChild.Parent = self.curr_node
            self.Increament()           
        else:
##            print("LC exists, recursion")
            self.curr_node = self.curr_node.LeftChild
            self.Assign(TC, "R")
            
    def GoRight(self, TC):        
        if not self.curr_node.RightChild:
##            print("Creating RC")
            self.curr_node.RightChild = node(TC)
            self.curr_node.RightChild.Parent = self.curr_node
            self.Increament()           
        else:
##            print("RC exists, recursion")
            self.curr_node = self.curr_node.RightChild
            self.Assign(TC, "R")

    def Increament(self):
        self.nodes += 1                
            
    def HasChild(self, sn, child):
        if child == "LC":            
            if sn.LeftChild:
                return True            
            else:
                return False           
        else:          
            if sn.RightChild:
                return True           
            else:
                return False
            
    def Search(self, value, search_node = None):
        """ Returns The Node Having The Given Value"""
        if not search_node:
            search_node = self.root_node            
        if value == search_node.value:
            return search_node        
        elif value <= search_node.value:
##            print("{} < {}".format(value, search_node.value))           
            if search_node.hasLeftChild():              # self.HasChild(search_node, "LC"):
                return self.Search(value, search_node.LeftChild)            
            else:
                return False           
        elif value > search_node.value:
##            print("{} > {}".format(value, search_node.value))           
            if search_node.hasRightChild():     # self.HasChild(search_node, "RC"):
                return self.Search(value, search_node.RightChild)            
            else:
                return False

    def GetRootChilds(self):
        """Root and it's children"""
##        try:
##            print("Root: {}".format(self.root_node.value))
##        except (NameError, AttributeError):
##            print("No Root!")
##            
##        try:
##            print("Left Child: ".format(self.root_node.LeftChild))
##        except NameError:
##            print("The Root Does Not Have A Left Child")
##
##        try:
##            print("Right Child: ".format(self.root_node.RightChild))
##        except NameError:
##            print("The Root Does Not Have A Right Child")
        print("Root: {}".format(self.root_node.value))
        if self.root_node.hasLeftChild(): # self.HasChild(self.root_node, "LC"):
            print("Left Child: {}".format(self.root_node.LeftChild.value))
        else:
            print("No Left Child")
        if self.root_node.hasRightChild(): # self.HasChild(self.root_node, "RC"):
            print("Right Child: {}".format(self.root_node.RightChild.value))
        else:
            print("No Right Child")
                       
    def Tree(self):
        self.GetLevel()
        print("Levels : {} \nNodes : {}".format(self.level, self.nodes))

    def GetMin(self, glc = None):
        if glc == None:
            glc = self.root_node
        minimum = glc.value
        if glc.hasLeftChild(): # self.HasChild(glc, "LC"):
            return self.GetMin(glc.LeftChild)
        return  minimum

    def GetMax(self, grc = None):
        if grc == None:
            grc = self.root_node
        maximum = grc.value
        if grc.hasRightChild(): # self.HasChild(grc, "RC"):
            return self.GetMax(grc.RightChild)
        return maximum

    def ParentsWhichChild(self, child):
        parent = child.Parent
        if parent.LeftChild is child:
            return "Left"
        else:
            return "Right"

    def GetMinNode(self, glc):
        if self.HasChild(glc, "LC"):
            return self.GetMinNode(glc.LeftChild)
        return  glc
    
    def Remove(self, value):
        """Removes the node with the given value"""
        TR = self.Search(value)
        #Childs
        l = TR.hasLeftChild() #self.HasChild(TR, "LC")
        r = TR.hasRightChild() #self.HasChild(TR, "RC")
        removed = False
        while not removed:
            #Case 0   Has No Child
            if not l and not r:
                if self.ParentsWhichChild(TR) == "Left":
                    TR.Parent.LeftChild = None
                    del TR
                    break
                else:
                    TR.Parent.RightChild = None
                    del TR
                    break
            
            #Case 1 Has Only Left Child
            if l and not r:
                if self.ParentsWhichChild(TR) == "Left":
                    TR.Parent.LeftChild = TR.LeftChild
                    del TR
                    break
                else:
                    TR.Parent.RightChild = TR.LeftChild
                    del TR
                    break
            
            #Case 2  Has Only Right Child
            if not l and r:
                if self.ParentsWhichChild(TR) == "Left":
                    TR.Parent.LeftChild = TR.RightChild
                    del TR
                    break
                else:
                    TR.Parent.RightChild = TR.RightChild
                    del TR
                    break

            #Case 3  Has Both The Childs
            if l and r:
                RW = self.GetMinNode(TR.RightChild)
                lc = TR.LeftChild
                rc = TR.RightChild
                wctr = self.ParentsWhichChild(TR)
                wcrw = self.ParentsWhichChild(RW)
                if wcrw == "Left":
                    RW.Parent.LeftChild = None
                else:
                    RW.Parent.RightChild = None
                RW.LeftChild = lc
                RW.RightChild = rc
                TR.LeftChild.Parent = RW
                TR.RightChild.Parent =  RW
                RW.Parent = TR.Parent
                if wctr == "Left":
                    TR.Parent.LeftChild = RW
                    del TR
                    break
                else:
                    TR.Parent.RightChild = RW
                    del TR
                    break


    def Process(self, tbp):
        print(tbp.value)

    def PreOrderTraversal(self, node = None):       			# DLR
        if not node:
            node = self.root_node
        
        print(node.value)

        if node.hasLeftChild(): #self.HasChild(node,"LC"):
            self.PreOrderTraversal(node.LeftChild)
        

        if node.hasRightChild(): #self.HasChild(node,"RC"):
            self.PreOrderTraversal(node.RightChild)

    def InOrderTraversal(self, node = None): #LDR
        if not node:
            node = self.root_node

        if node.hasLeftChild(): # self.HasChild(node, "LC"):
            self.InOrderTraversal(node.LeftChild)

        print(node.value)

        if node.hasRightChild(): #self.HasChild(node, "RC"):
            self.InOrderTraversal(node.RightChild)


    def PostOrderTraversal(self, node = None):   #LRD
        if not node:
            node = self.root_node

        if node.hasLeftChild(): #self.HasChild(node, "LC"):
            self.PostOrderTraversal(node.LeftChild)

        if node.hasRightChild(): #self.HasChild(node, "RC"):
            self.PostOrderTraversal(node.RightChild)

        print(node.value)

    def goLevelWise(self, node):  # BFS
        has_left_child, has_right_child = 0, 0

        if not node:
            node = self.root_node

        if node.hasLeftChild():
            self.levels.append(node.getLeftChild().value)
            has_left_child = 1

        else:
            self.levels.append(" ")

        if node.hasRightChild():
            self.levels.append(node.getRightChild().value)
            has_right_child = 1

        else:
            self.levels.append(" ")

        if has_left_child:
            self.goLevelWise(node.getLeftChild())

        if has_right_child:
            self.goLevelWise(node.getRightChild())


    
    def Visualize(self):
        self.levels.append(self.root_node.value)
        self.goLevelWise(self.root_node)
        s = " "

        for level in self.levels:
            print(level)

    def GetLevel(self):
        pass

# t.Assign([12,24,8,36,18,10])
