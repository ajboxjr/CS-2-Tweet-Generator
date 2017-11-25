class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class LinkedList(object):
    """Initialize this linked list and append the given items, if any."""
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def append(self,data):
        """Add Node with data to the end of linked list and set to tail"""
        # setting tail and head 
        if self.is_empty():
            self.head = self.tail = Node(data)
            print('added head')
            return True
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            self.tail = curr.next = Node(data)
            
    def prepend(self,data):
        """Add Node to begining of Linkelist. Set it to head"""
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            curr = self.head
            new = Node(data)
            new.next = curr
            curr.prev = new
            self.head = new

    def replace(self,item, quality):
        if self.head:
            curr = self.head
            while curr:
                if quality(curr.data):
                    curr.data = item
                else:
                    curr = curr.next
        else:
            return None
                    

    def find(self, quality):
        curr = self.head
        if curr != None:
            while curr:
                if quality(curr.data):
                    print("found {} at {}".format(curr.data, curr))
                    return curr.data
                else:
                    curr = curr.next
        else:
            print("not found")
            return None

    

    def delete(self,item):
        """Delete a node based on it's data value"""
        #Delete first node
        if self.head:
            prev = self.head
            if head.data == item:
                self.head = head.next
            #The other nodes
            else:
                prev = self.head
                curr = prev.next
                while curr.next:
                    print("prev {} , cur {}".format(prev.data, curr.data))
                    if curr.data == item:
                        prev.next = curr.next
                        return "deleted {}".format(curr)
                    else:
                        prev = prev.next
                        curr = prev.next
                print(curr.data)
                print(prev.data)
                if curr.data == item:
                    self.tail = prev    
                    prev.next = None
                else:
                    print("{} is not in the linkedlist".format(item))
                    return ValueError
        else:
            return ValueError

    def get_node(self, index):
        """(ABstract). Get element based on index."""
        if self.is_empty():
            return -1
        else:
            if index == 0:
                return self.head
            else:
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


    def length(self):
        """Return the legth of the code"""
        idx = 1
        if self.head == None:
            return 0
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
                idx +=1
            return idx

    def __str__(self):
            """Return a formatted string representation of this linked list."""
            items = ['({!r})'.format(item) for item in self.items()]
            return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
            """Return a string representation of this linked list."""
            return 'LinkedList({!r})'.format(self.items())

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
