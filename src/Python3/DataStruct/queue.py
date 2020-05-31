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
    def __init__(self):
        self.__array = []

    def __len__(self):
        return len(self.__array)

    def is_empty(self):
        return self.__array is None

    def Enqueue(self, data):
        if type(data) == int:
            self.__array.append(data)
            self.__upAdjust()
        else:
            raise ValueError("PriorityQueue -> Enqueue(): data is error.")

    def Dequeue(self):
        l: int = self.__len__()
        if l == 0:
            raise ValueError("PriorityQueue -> Enqueue(): Queue is Empty.")
        elif l == 1:
            return self.__array.pop()
        else:
            temp = self.__array[0]
            self.__array[0] = self.__array.pop()
            self.__downAdjust()
            return temp

    def __upAdjust(self):
        childIndex = self.__len__() - 1
        parentIndex = (childIndex - 1) >> 1
        temp = self.__array[childIndex]
        while childIndex > 0 and temp > self.__array[parentIndex]:
            self.__array[childIndex] = self.__array[parentIndex]
            childIndex = parentIndex
            parentIndex >>= 1
            self.__array[childIndex] = temp

    def __downAdjust(self):
        parentIndex = 0
        temp = self.__array[parentIndex]
        childIndex = 1
        while childIndex < self.__len__():
            if childIndex + 1 < self.__len__() and self.__array[childIndex + 1] > self.__array[childIndex]:
                childIndex += 1
            if temp >= self.__array[childIndex]:
                break
            self.__array[parentIndex] = self.__array[childIndex]
            parentIndex = childIndex
            childIndex = 2 * childIndex + 1
        self.__array[parentIndex] = temp

    def print(self, sep=' ', end="\n"):
        print(sep.join(self.__array))
        print(end=end)
