from node import Node


class LinkedList:
    """
    head: the beginning of the node
    tail: the end of the node
    """

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        """
        previous: the position before the new node is pointed
        runner: the position after the new node is pointed

        Node structure as an example of else case
            1X(2) -> 2x(4) -> 3x(5) -> 4x(7) -> 5x(9) -> 6x(10)
        When insert_node is called and value is 6, the previous is 1x(2) and runner is 2x(4).
        This is the first pair of nodes that we will analyze in order to determine if the new node should be inserted between them.
        If not, we update the values of previous and runner to the next pair of nodes to move forward in the linked list using the pointers.
        In this case, when previous and runner are 3x and 4x, respectively, the value 6 is inserted between 3x and 4x.

        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next

            new_node.next = runner
            previous.next = new_node

    def print_list_items(self):
        if self.head is None:
            print('Empty')
        else:
            runner = self.head
            while runner is not None:
                print(runner.value, end=' ')
                runner = runner.next
            print()

    def count_nodes(self):
        '''
        # iterative method is a little bit more efficient in terms of performance than recursive method.
        # iterative implementation
        count = 0
        runner = self.head

        while runner is not None:
            count += 1
            runner = runner.next

        return count
        '''

        return self.count_nodes_recursive(self.head)

    def count_nodes_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes_recursive(node.next)





