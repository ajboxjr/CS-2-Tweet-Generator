class Node(object):
    def __init__(self, data):
        """Initialize the node with a data and a pointer(next)"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)
"""
TO lower space time complexity added abstract len function(self.len)
"""
class LinkedList(object):
    """Initialize this linked list and append the given items, if any."""
    def __init__(self, items=None):
        self.head = None
        self.tail = None 
        #Alternative way of calculating length/ rather than itteration
        self.len = 0 
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

    def __iter__(self):
        """Returning the start node for the self"""
        self.node = self.head
        return self

    def __next__(self):
        """Return the current node in instance of the linked list """ # Kaichi
        # 1. set current node as variable 
        # update the itterator to next node(for next update)
        # 2. current node 
        if self.node is not None:
            node = self.node
            self.node = self.node.next
            return node
        else:
            raise StopIteration

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        # Loop until node is None, which is one node too far past tail
        for node in self:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None and self.tail is None

    def append(self,data):
        """Add Node with data to the end of linked list and set to tail"""
        if self.is_empty():
        # setting tail and head to Node 
            self.head = Node(data)
            self.tail = self.head
            self.len +=1
        else:
            #Use self.tail to elimitate itterating
            #1. Create Node
            #2. Set tail.next to Node
            #3. Set tail to node
            last = self.tail
            node = Node(data)
            last.next = node 
            self.tail = node 
            self.len += 1
        print(self)

    def prepend(self,data):
        """Add Node to begining of Linkelist. Set it to head"""
        if self.is_empty():
            self.head = Node(data)
            self.tail = self.head
            self.len += 1
        else:
            #1. Create a node
            #2. Set node next to head
            #3. Set head to the node 
            new = Node(data)
            self.len += 1
            new.next = self.head
            self.head = new

    def replace(self,item, quality):
        """Find item and set it's prev(if one) to item and item prev.next to item"""
        curr = self.head
        while curr:
            if quality(curr.data):
                curr.data = item
                return True
            else:
                curr = curr.next
        return False

                    

    def find(self, quality):
        for node in self:
            if quality(node.data): #Node(data)[0]
                return node.data 
        return None

    

    def delete(self,item):
        """Delete a node based on it's data value"""
        #Delete first node
        if self.is_empty():
            return ValueError
        else:
            if self.head.data == item:
                self.head = self.head.next
                self.len -=1
                if self.head == None:
                    self.tail = None
                return "Deleted first node"
            #The other nodes
            else:
                #IF item found prev.next will be set to curr.next(erasing the node)
                prev = self.head
                curr = prev.next
                while curr is not None:
                    print("prev {} , cur {}".format(prev.data, curr.data))
                    if curr.data == item:
                        prev.next = curr.next
                        self.len -=1
                        if prev.next == None:
                            print('yaah')
                            self.tail = prev
                        return "deleted {}".format(curr)
                    else:
                        prev = prev.next
                        curr = prev.next
                if curr == None:
                    self.tail = None
                else:
                    print("{} is not in the linkedlist".format(item))
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
        """
        This solution is O(N)
        idx = 0
        for _ in self:
            idx +=1
        return idx
        """
        return self.len


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
