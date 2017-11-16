class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head_data=None):
        if head_data:
            self.head = Node(head_data)

    def append(self,data):
        if self.head == None:
            self.head = Node(data)
            print('added head')
            return True
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
            return True

    def delete(self,index):
        curr = self.head
        if (index) == 0:
            return self.head
        for _ in range(index-1):
            curr = curr.next
        curr.next = curr.next.next

    def get_index(self, index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
            if curr == None:
                return -1
        return curr.data
    def length(self):
        idx = 1
        if self.head == None:
            return 0
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
                idx +=1
            return idx

   
if __name__ == '__main__':
    listz = LinkedList()
    listz.append(1)
    listz.append(2)
    listz.append(3)
    print(listz)
    listz.get_index(0)
    listz.delete(2)
    listz.append(55)
    listz.append(22)
    print(listz)
    listz.delete(3)
    print(listz)
    print(listz.length())
