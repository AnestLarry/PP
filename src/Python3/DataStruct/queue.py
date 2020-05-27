class Queue:
    class Node:
        def __init__(self, data=None, prev=None, Next=None):
            self.data = data
            self.prev = prev
            self.next = Next

    def __init__(self, node=None):
        self.__front: Queue.Node = node
        self.__rear: Queue.Node = node
        self.__len: int = 0

    def __len__(self):
        return self.__len

    def is_empty(self):
        return self.__front is None

    def Enqueue(self, data):
        if self.__front is None:
            self.__front = self.__rear = self.Node(data)
        else:
            self.__rear.next = self.Node(data, self.__rear)
            self.__rear = self.__rear.next
        self.__len += 1

    def Dequeue(self):
        if self.__front is None:
            raise LookupError("Empty Queue.")
        else:
            node = self.__front
            node.prev = None
            self.__front = node.next
            self.__len -= 1
            return node.data

    def print(self, sep=' ', end="\n"):
        cur = self.__front
        while cur:
            print(cur.data, end=sep)
            cur = cur.next
        print(end=end)


class PriorityQueue:
    def __init__(self, isMaxPriorityQueue):
        self.__array = []
        self.__isMaxPriorityQueue = isMaxPriorityQueue

    def __len__(self):
        return len(self.__array)

    def is_empty(self):
        return self.__array is None

    def Enqueue(self, data):
        if type(data) == "int":
            self.__array.append(data)
            i = len(self.__array)>>1
            while i>-1:
                if self.__array[i] > 
        else:
            raise ValueError("PriorityQueue -> Enqueue(): data is error.")
        # if self.__front is None:
        #     self.__front = self.__rear = self.Node(data)
        # else:
        #     self.__rear.next = self.Node(data, self.__rear)
        #     self.__rear = self.__rear.next
        # self.__len += 1

    def Dequeue(self):
        if self.__front is None:
            raise LookupError("Empty Queue.")
        else:
            node = self.__front
            node.prev = None
            self.__front = node.next
            self.__len -= 1
            return node.data

    def print(self, sep=' ', end="\n"):
        for i in self.__array:
            print(i, end=sep)
        print(end=end)
