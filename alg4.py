#   一个无序单链表的实现（比较简单）
#   class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        if self.search(item):
            while not found:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            print('This number %d is not in list.' % item)

    def __str__(self):
        return "This list contains %d nodes." % self.size()

    def append(self, item):
        temp = Node(item)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(temp)

    def index(self, item):
        current = self.head
        index_num = 0
        if self.search(item):
            while current.getData() != item:
                current = current.getNext()
                index_num += 1
            return index_num
        else:
            return 'No this number'

    def pop(self, *args):
        current = self.head
        if len(args) == 0:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
        else:
            pos = args[0]
            index_num = 0
            if 0 < pos < (self.size()-1):
                while index_num != pos:
                    previous = current
                    current = current.getNext()
                    index_num += 1
                previous.setNext(current.getNext())
            else:
                print('out of range!')

    def insert(self, pos, item):
        if 0 < pos <= (self.size()-1):
            temp = Node(item)
            current = self.head
            index_cur = 0
            while index_cur < pos:
                previous = current
                current = current.getNext()
                index_cur += 1
            previous.setNext(temp)
            temp.setNext(current)
        else:
            print('Wrong position')

    def slice(self, start, stop):
        if 0 < start < stop < (self.size()-1):
            current = self.head
            resList = []
            index_node = 0
            while index_node != start:
                current = current.getNext()
                index_node += 1
            index_node = 0
            while index_node < (stop-start):
                resList.append(current.getData())
                current = current.getNext()
                index_node += 1
            return resList
            pass
        else:
            print('Wrong range!')
