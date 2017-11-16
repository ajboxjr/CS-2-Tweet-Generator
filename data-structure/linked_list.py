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
        if items:
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
        if self.is_empty():
            self.head = self.tail = Node(data)
            print('added head')
            return True
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            self.tail = curr.next = Node(data)
            

    def delete(self,index):
        """Get Node a set it's previous to next and next to prev"""
        if (index) == 0:
            return self.head
        #Get Previous node
        for _ in range(index-1):
            curr = curr.next
        print(curr)
        curr.next = curr.next.next
            
    def get_node(self, index):
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
