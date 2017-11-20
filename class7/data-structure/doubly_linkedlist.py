class Node(object):
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class DoublyLinkedList(object):
    """Create a linked list. Can pass in array of data items(optional)"""
    def __init__(self, data_items=None):
        self.head = None
        self.tail = None
        if data_items is not None:
            for item in data_items:
                self.append(item)

    def append(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            curr = self.tail
            new = Node(data)
            self.tail.next, new.prev = new, curr
            self.tail = new
    
    def prepend(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head 
        else:
            curr = self.head
            new = Node(data)
            new.next, curr.prev = curr, new
            self.head = new

    def get_node(self, index):
        if self.head == None:
            return -1
        else:
            if index == 0:
                return self.head
            elif index > 0:
                x = 0 
                curr = self.head
                while x < index:
                    if curr.next != None:
                        print(curr.data)
                        curr = curr.next
                        x+=1
                    else:
                        print("index out of bounds")
                        return -2
                print(curr.data)
                return curr
            elif index < 0:
                x = -1
                curr = self.tail
                while x > index:
                    if curr.prev != None:
                        print(curr.data)
                        curr = curr.prev
                        x-=1
                    else:
                        print("index out of bounds")
                        return -2
                print(curr.data)
                return curr
                    

    def delete(self, item):
        """DeleteNode based on item data"""
        prev = self.head
        if prev.data == item:
            self.head = prev.next
            if self.head == None:
                self.tail = None
        while prev.next:
            curr = prev.next
            if curr.data == item:
                print(curr.data)
                if curr.next ==None:
                    self.tail = None
                else:
                    pass
                prev.next = curr.next
            prev = prev.next

    def deleteNext(self, index):
        pass
    def __str__(self):
        data = ""
        curr = self.head
        while curr != None:
            data += str(curr.data)+ " "
            curr = curr.next
        return data
if __name__ == '__main__':
    double = DoublyLinkedList()
    double.append(5)
    double.append(6)
    double.append(6)
    double.append(6)
    double.append(6)
    print(double)
