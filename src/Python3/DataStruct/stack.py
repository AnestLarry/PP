from DataStruct.linkedlist import *


class Stack:
    def __init__(self):
        self.__ll = LinkedList()

    def __len__(self):
        return len(self.__ll)

    def push(self, data):
        self.__ll.append(data)

    def pop(self):
        return self.__ll.pop()

    def getTop(self):
        return self.__ll.getItem()

    def is_empty(self):
        return self.__ll.is_empty()

    def travel(self):
        return self.__ll.travel()

    def print(self):
        self.__ll.print()
