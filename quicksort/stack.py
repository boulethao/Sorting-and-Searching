#!/usr/bin/env python

class Stack():
    """
    Simple stack implementation
    """
    def __init__(self):
        """
        Initialize the list of items of the stack
        """
        self.list = []

    def push(self, item):
        """
        Push an item onto the stack
        :param item: The item to push
        :return:
        """
        self.list.append(item)

    def pop(self):
        """
        Pop an item from top of the stack
        :return: The popped item
        """
        if len(self.list) > 0:
            item = self.list.pop()
            return item
        else:
            raise "ERROR: Stack is empty."

    def peek(self):
        """
        Peek on top of the stack
        :return: the item on top of the stack
        """
        if len(self.list) > 0:
            return self.list[len(self.list)-1]
        else:
            return None

    def is_empty(self):
        """
        Check if the stack is empty
        :return: True if empty / False if not empty
        """
        return len(self.list) == 0

    def size(self):
        """
        Get the size of the stack
        :return:
        """

        return len(self.list)

