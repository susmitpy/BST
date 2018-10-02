class Queue:
    def __init__(self):
        self.my_queue = []

    def push(self, element):
        self.my_queue.append(element)

    def pop(self):
        return self.my_queue.pop(0)

    def is_empty(self):
        if len(self.my_queue) > 0:
            return False
        return True

    def has_element(self):
        return not self.is_empty()
