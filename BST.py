from node import Node
from queue import Queue
import logging


class BST:
    def __init__(self):
        self.level = 0
        self.nodes = 0
        self.levels = []
        self.queue = Queue()
        self.root_node = None
        self.curr_node = None

    def assign(self, value, current_node=None):
        if isinstance(value, list):
            for i in range(len(value)):
                self.assign(value[i])
        else:
            if not self.nodes:
                self.root_node = Node(value)
                self.curr_node = Node(value)
                self.increment()
            else:
                if not current_node:
                    self.curr_node = self.root_node
                self.compare(self.curr_node.value, value)

    def compare(self, p, tc):
        if self.nodes != 0:
            if p < tc:
                self.go_right(tc)
            else:
                self.go_left(tc)

    def go_left(self, tc):
        if not self.curr_node.LeftChild:
           
            self.curr_node.LeftChild = Node(tc)
            self.curr_node.LeftChild.Parent = self.curr_node
            self.increment()
        else:
            
            self.curr_node = self.curr_node.LeftChild
            self.assign(tc, "R")

    def go_right(self, tc):
        if not self.curr_node.RightChild:
     
            self.curr_node.RightChild = Node(tc)
            self.curr_node.RightChild.Parent = self.curr_node
            self.increment()
        else:
           
            self.curr_node = self.curr_node.RightChild
            self.assign(tc, "R")

    def increment(self):
        self.nodes += 1

    def search_node_by_value(self, value, search_node=None):
        """ Returns The Node Having The Given Value"""
        if not search_node:
            search_node = self.root_node
        if value == search_node.value:
            return search_node
        elif value <= search_node.value:
            if search_node.hasLeftChild():
                return self.search_node_by_value(value, search_node.LeftChild)
            else:
                return False
        elif value > search_node.value:
            if search_node.hasRightChild():
                return self.search_node_by_value(value, search_node.RightChild)
            else:
                return False

    def get_root_childs(self):
        """Root and it's children"""
        print("Root: {}".format(self.root_node.value))
        if self.root_node.hasLeftChild():  # self.HasChild(self.root_node, "LC"):
            print("Left Child: {}".format(self.root_node.LeftChild.value))
        else:
            print("No Left Child")
        if self.root_node.hasRightChild():  # self.HasChild(self.root_node, "RC"):
            print("Right Child: {}".format(self.root_node.RightChild.value))
        else:
            print("No Right Child")

    def tree(self):
        self.get_level()
        print("Levels : {} \nNodes : {}".format(self.level, self.nodes))

    def get_min(self, glc=None):
        if glc is None:
            glc = self.root_node
        minimum = glc.value
        if glc.hasLeftChild():  # self.HasChild(glc, "LC"):
            return self.get_min(glc.LeftChild)
        return minimum

    def get_max(self, grc=None):
        if grc is None:
            grc = self.root_node
        maximum = grc.value
        if grc.hasRightChild():  # self.HasChild(grc, "RC"):
            return self.get_max(grc.RightChild)
        return maximum

    def parents_which_child(self, child):
        parent = child.Parent
        if parent.LeftChild is child:
            return "Left"
        else:
            return "Right"

    def get_min_node(self, glc):
        if glc.hasLeftChild():
            return self.get_min_node(glc.LeftChild)
        return glc

    def remove_node(self, value):
        """Removes the node with the given value"""
        tr = self.search_node_by_value(value)
        has_left_child = tr.hasLeftChild()
        has_right_child = tr.hasRightChild()
        removed = False
        while not removed:
            # Case 0   Has No Child
            if not has_left_child and not has_right_child:
                if self.parents_which_child(tr) == "Left":
                    tr.Parent.LeftChild = None
                    del tr
                    break
                else:
                    tr.Parent.RightChild = None
                    del tr
                    break

            # Case 1 Has Only Left Child
            if has_left_child and not has_right_child:
                if self.parents_which_child(tr) == "Left":
                    tr.Parent.LeftChild = tr.LeftChild
                    del tr
                    break
                else:
                    tr.Parent.RightChild = tr.LeftChild
                    del tr
                    break

            # Case 2  Has Only Right Child
            if not has_left_child and has_right_child:
                if self.parents_which_child(tr) == "Left":
                    tr.Parent.LeftChild = tr.RightChild
                    del tr
                    break
                else:
                    tr.Parent.RightChild = tr.RightChild
                    del tr
                    break

            # Case 3  Has Both The Childs
            if has_left_child and has_right_child:
                rw = self.get_min_node(tr.RightChild)
                lc = tr.LeftChild
                rc = tr.RightChild
                wctr = self.parents_which_child(tr)
                wcrw = self.parents_which_child(rw)
                if wcrw == "Left":
                    rw.Parent.LeftChild = None
                else:
                    rw.Parent.RightChild = None
                rw.LeftChild = lc
                rw.RightChild = rc
                tr.LeftChild.Parent = rw
                tr.RightChild.Parent = rw
                rw.Parent = tr.Parent
                if wctr == "Left":
                    tr.Parent.LeftChild = rw
                    del tr
                    break
                else:
                    tr.Parent.RightChild = rw
                    del tr
                    break

    def process(self, tbp):
        print(tbp.value)

    def pre_order_traversal(self, node=None):  # DLR
        if not node:
            node = self.root_node

        print(node.value)

        if node.hasLeftChild():  # self.HasChild(node,"LC"):
            self.pre_order_traversal(node.LeftChild)

        if node.hasRightChild():  # self.HasChild(node,"RC"):
            self.pre_order_traversal(node.RightChild)

    def in_order_traversal(self, node=None):  # LDR
        if not node:
            node = self.root_node

        if node.hasLeftChild():  # self.HasChild(node, "LC"):
            self.in_order_traversal(node.LeftChild)

        print(node.value)

        if node.hasRightChild():  # self.HasChild(node, "RC"):
            self.in_order_traversal(node.RightChild)

    def post_order_traversal(self, node=None):  # LRD
        if not node:
            node = self.root_node

        if node.hasLeftChild():  # self.HasChild(node, "LC"):
            self.post_order_traversal(node.LeftChild)

        if node.hasRightChild():  # self.HasChild(node, "RC"):
            self.post_order_traversal(node.RightChild)

        print(node.value)

    def add_to_levels(self):

        while self.queue.has_element():
            first = self.queue.pop()
            self.queue.push(first.getLeftChild())
            self.queue.push(first.getRightChild())

    def go_level_wise(self, elem):  # BFS
        if isinstance(elem, Node):
            self.levels.append(elem.value)
        else:
            self.levels.append(" ")

        self.queue.push(elem.getLeftChild())
        self.queue.push(elem.getRightChild())

        self.add_to_levels()

    def visualize(self):
        self.go_level_wise(self.root_node)
        s = " "

        for level in self.levels:
            print(level)

    def get_level(self):
        pass

# t.Assign([12,24,8,36,18,10])
