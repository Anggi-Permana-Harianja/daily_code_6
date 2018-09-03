'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
'''

'''
we start by how normal double linkedlist looks like
'''
class Node(object):
	def __init__(self, data, prev_node = None, next_node = None):
		self.data = data
		self.prev_node = prev_node
		self.next_node = next_node

class Double_LinkedList(object):
	def __init__(self, node):
		self.first_node = node
		self.last_node = node

	def push(self, node):
		node.next_node = self.first_node
		node.prev_node = None
		self.first_node.prev_node = node
		self.first_node = node

	def pop(self):
		last_node = self.last_node
		tobe_last_node = self.last_node.prev_node
		tobe_last_node.next_node = None
		self.last_node.prev_node = None

		self.last_node = last_node

		return last_node.data

	def remove(self, node):
		next_node = node.next_node
		prev_node = node.prev_node

		prev_node.next_node = next_node
		next_node.prev_node = prev_node

		node.next_node = node.prev_node = None

		return node.data

	def print(self):
		current_node = self.first_node

		while current_node:
			print(current_node.data)
			current_node = current_node.next_node


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
nodes = [node1, node2, node3, node4]

DLL = Double_LinkedList(node1)

DLL.push(node2)
DLL.push(node3)
DLL.push(node4)
DLL.print()
print('---------------')

print(DLL.pop())
print('----------------')
DLL.print()
print('---------------')

print(DLL.remove(node3))
print('---------------')
DLL.print()
print('##############')

'''
we now implement the XOR linked list
'''

class XOR_Node(object):
	def __init__(self, data, prev_node_index = -1, next_node_index = -1):
		self.data = data
		self.both = prev_node_index ^ next_node_index

	def next_node_function(self, prev_node_index):
		return self.both ^ prev_node_index

	def prev_node_function(self, next_node_index):
		return self.both ^ next_node_index

class XOR_LinkedList(object):
	def __init__(self):
		self.memory = [XOR_Node(0, -1, -1)]

	def head(self):
		return 0, -1, self.memory[0] #head index, prev_node_index, head node

	def push(self, data):
		current_node_index, prev_node_index, current_node = self.head()

		while True:
			next_node_index = current_node.next_node_function(prev_node_index)

			if next_node_index == -1:
				break

			prev_node_index, current_node_index = current_node_index, next_node_index
			current_node = self.memory[current_node_index]

		#allocate for incoming nodes
		new_node_index = len(self.memory)
		current_node.both = prev_node_index ^ new_node_index
		self.memory.append(XOR_Node(data, current_node_index, -1))

	def get(self, index):
		current_node_index, prev_node_index, current_node = self.head()

		for _ in range(index + 1):
			next_node_index = current_node.next_node_function(prev_node_index)
			prev_node_index, current_node_index = current_node_index, next_node_index
			current_node = self.memory[current_node_index]

		return self.memory[current_node_index].data

	def print(self):
		for i in range(len(self.memory) - 1):
			print(self.get(i).data)

XOR_DLL = XOR_LinkedList()
node1 = XOR_Node(1)
node2 = XOR_Node(2)
node3 = XOR_Node(3)

XOR_DLL.push(node1)
XOR_DLL.push(node2)
XOR_DLL.push(node3)

XOR_DLL.print()
print('--------------')

print(XOR_DLL.get(0).data)