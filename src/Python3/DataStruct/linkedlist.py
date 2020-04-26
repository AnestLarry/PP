class LinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self, node=None):
        self.__head = node
        self.__tail = node
        self.__len = 0

    def __len__(self):
        return self.__len

    def __getItem(self, index):
        node = self.__head
        for i in range(self.__len):
            if i == index:
                return node
            node = node.next

    def is_empty(self):
        return self.__head is None

    def append(self, data):
        self.insert(data)

    def insert(self, data, index=-1):
        if index < 0:
            index = self.__len + index + 1
        if index > self.__len:
            raise IndexError("Index out of range.")
        if self.__head is None:
            self.__head = self.__tail = self.Node(data)
        elif index == 0:
            self.__head.prev = self.Node(data, next=self.__head)
            self.__head = self.__head.prev
        elif index == self.__len:
            self.__tail.next = self.Node(data, self.__tail)
            self.__tail = self.__tail.next
        else:
            node = self.__getItem(index)
            node.prev.next = self.Node(data, node.prev, node)
            node.prev = node.prev.next
        self.__len += 1

    def pop(self, index=-1):
        if self.__head is None:
            raise LookupError("Empty Chain.")
        if index < 0:
            index = self.__len + index
        if not index < self.__len:
            raise IndexError("Index out of range.")
        node = self.__getItem(index)
        if index == 0:
            node.prev = None
            self.__head = node.next
        elif index == self.__len - 1:
            node.prev.next = None
            self.__tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.__len -= 1
        return node.data

    def travel(self):
        cur = self.__head
        while cur is not None:
            yield cur.data
            cur = cur.next

    def print(self):
        for data in self.travel():
            print(data, end=" ")
        print()
 