
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
# test ----'''

# test with char----'''
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

node_char4 = Node('Code')
node_char3 = Node('Hello', node_char4)
node_char2 = Node('World', node_char3)
node_char1 = Node('Python', node_char2)
print(node_char1.value, end=' ')
print(node_char2.value, end=' ')
print(node_char3.value, end=' ')
print(node_char4.value, end=' ')

