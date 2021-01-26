class Node(object):
	def __init__(self, value = 0, left = None, right=None):
		self.value = value
		self.left = left
		self.right = right

class Tree:
	def createNode(self, value):
		return Node(value)

	def insert(self, node, value):
		if node is None:
			return self.createNode(value)
		else:
			if value < node.value:
				node.left = self.insert(node.left, value)
			elif value > node.value:
				node.right = self.insert(node.right, value)

		return node

	def printTree(self, node):
		if node is not None:
			print(node.value)
			self.printTree(node.left)
			self.printTree(node.right)

	def search(self, value, node):
		try:
			if value < node.value:
				self.search(value, node.left)
			elif value > node.value:
				self.search(value, node.right)
			elif value == node.value:
				print("Node is found")
		except:
			print("Node is not in the list")

tree = Tree()
root = tree.createNode(10)

nodes = [5,12,2,3,6,15,13,14,8,0,20]

for node in nodes:
	tree.insert(root, node)

tree.printTree(root)
tree.search(5,root)
tree.search(100,root)
