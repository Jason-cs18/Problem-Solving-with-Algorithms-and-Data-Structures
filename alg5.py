#   一个有序单链表的实现（比较简单）
class Node:
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


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def remove(self, item):
        if self.search(item):
            current = self.head
            while current.getData() != item:
                previous = current
                current = current.getNext()
            previous.setNext(current.getNext())
        else:
            print('There is no this item')

    def index(self, item):
        if self.search(item):
            current = self.head
            count = 0
            while current.getData() != item:
                current = current.getNext()
                count += 1
            return count
        else:
            print('There is no this item')

    def pop(self, *args):
        current = self.head
        if len(args) == 0:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
        else:
            pos = args[0]
            if 0< pos < (self.size()-1):
                curr_index = 0
                while curr_index != pos:
                    previous = current
                    current = current.getNext()
                    curr_index += 1
                previous.setNext(current.getNext())
            else:
                print('Wrong position!')
