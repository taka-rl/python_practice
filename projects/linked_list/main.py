
from node import Node

'''
node_2 = Node(3)
node_1 = Node(5, node_2)
print(node_1.value)

# node_1 -> node_2
print(node_2.value)
print(node_1.next is node_2)  # True
print(node_1.next)  # return node_2 object memory location
print(node_2)
print(node_2.next)  # None

# test ----
# node_a -> node_b -> node_c -> node_d
# node_a: value = "a", next = node_b
# node_b: value = "b", next = node_c
# node_c: value = "c", next = node_d
# node_d: value = "d", next = None

node_d = Node('d', None)
node_c = Node('c', node_d)
node_b = Node('b', node_c)
node_a = Node('a', node_b)

print('value:', node_a.value, 'next:', node_a.next)
print('value:', node_b.value, 'next:', node_b.next)
print('value:', node_c.value, 'next:', node_c.next)
print('value:', node_d.value, 'next:', node_d.next)

node_a.value = 'a1'
print('value:', node_a.value, 'next:', node_a.next)
node_d.next = node_a
print('node_a:', node_a)
print('value:', node_d.value, 'next:', node_d.next)
# test ----
'''

import time
from linked_list import LinkedList

# test ----
my_linked_list = LinkedList()
my_linked_list.insert_node(9)
print(my_linked_list.head)
print(my_linked_list.head.value)  # 9
# 1st: 9

my_linked_list.insert_node(3)
print(my_linked_list.head.value)  # 3
# 2nd: 3 -> 9

my_linked_list.insert_node(6)
print(my_linked_list.head.next.value)  # 6
# 3rd: 3 -> 6 -> 9
print(my_linked_list.head.value)  # 3
print(my_linked_list.head.next.value)  # 6
print(my_linked_list.head.next.next.value)  # 6

my_linked_list.insert_node(15)
# 4th: 3 -> 6 -> 9 -> 15
print(my_linked_list.head.next.next.next.value)
my_linked_list.print_list_items()
my_linked_list.delete_node(15)
my_linked_list.delete_node(6)
my_linked_list.print_list_items()

'''
start_time = time.time()
print(my_linked_list.count_nodes())
end_time = time.time()
print(f"Total execution time of iterative method: {end_time - start_time} second")
start_time = time.time()
print(my_linked_list.count_nodes_recursive(my_linked_list.head))
end_time = time.time()
print(f"Total execution time of recursive method: {end_time - start_time} second")


my_linked_list_null = LinkedList()
print(my_linked_list_null.count_nodes())
'''

# test ----'''
'''
# test with char----
my_linked_list_char = LinkedList()
my_linked_list_char.insert_node('Python')
my_linked_list_char.insert_node('World')
my_linked_list_char.insert_node('Hello')
my_linked_list_char.insert_node('Code')

# print(my_linked_list_char.head.value, end=' ')
# print(my_linked_list_char.head.next.value, end=' ')
# print(my_linked_list_char.head.next.next.value, end=' ')
# print(my_linked_list_char.head.next.next.next.value, end=' ')
# print()
my_linked_list_char.print_list_items()
print(my_linked_list_char.count_nodes())

print(my_linked_list_char.find_node('Python'))
print(my_linked_list_char.find_node('Python1'))
print(my_linked_list_char.delete_node('Code'))
my_linked_list_char.print_list_items()
'''

# test print reversibly
'''
How print_reversed method works:
- Recursive Call Structure
Imagine the linked list: 3 -> 5 -> 8 -> 15 -> 26 -> 35.
print_reversed() is called, which calls print_reversed_recursive(self.head).
The recursion goes as follows:
    print_reversed_recursive(node=3) calls print_reversed_recursive(node=5).
    print_reversed_recursive(node=5) calls print_reversed_recursive(node=8).
    This continues until print_reversed_recursive(node=35) calls print_reversed_recursive(node=None).
    
- Unwinding and Printing
Once node=None is reached, each call returns in the reverse order:
The print(node.value, end=' ') statement is executed in the reverse call order.
35, 26, 15, 8, 5, and 3 are printed, in that order.

How is this possible?
- Function call stack:
    Each time a function is called, it is pushed onto a call stack. When a function completes, 
    it is popped off the stack, and the control returns to the function that called it.
    The function calls are executed in a Last In, First Out (LIFO) manner, which means that 
    the most recent call (the last one made) is the first to complete and return.

- Recursive Function Flow: 
    In the case of recursion, each call to the recursive function adds another layer to the stack, 
    each with its own local variables and state. The deepest call (where the base condition is met) is completed first, 
    and then the function starts to return back through the stack, one layer at a time.

'''

my_linked_list1 = LinkedList()
my_linked_list1.insert_node(3)
my_linked_list1.insert_node(5)
my_linked_list1.insert_node(8)
my_linked_list1.insert_node(15)
my_linked_list1.insert_node(26)
my_linked_list1.insert_node(35)
my_linked_list1.print_reversed()


