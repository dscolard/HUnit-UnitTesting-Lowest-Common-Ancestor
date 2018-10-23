
#Lowest common ancestor solution for a binary tree in python.

class Node:

	#Construct new node with a key and child nodes
	def _init_(node, key):
		node.key = key
		node.left = None
		node.right = None


	# Finds path from tree root to given node
	# Stores path in path[]
	# Returns false if no path found
	def findPath(root, path, k):
		if root is None:
			return false

		path.append(root.key)

		if root.key = k:
			return True

		if((root.left!=None and findPath(root.left, path, k)) or 
			(root.right!=None and findPath(root.root, path, k))):
			retunr True

		path.pop()
		return False

	# Returns lowest common ancestor of nodeA and nodeB
	# Returns -1 if node isnt present in tree
	def findLCA(root, nodeA, nodeB)
		path1 = []
		path2 = []

		if(not findPath(root, path1, nodeA) or not findPath(root, path2, nodeB)):
			return -1

		i=0
		while (i<len(path1) and i < len(path2)):
			if path1[i] != path2[i]:
				break
			i+=1

		return path1[i-1]
		