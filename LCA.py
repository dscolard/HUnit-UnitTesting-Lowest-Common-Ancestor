
#Lowest common ancestor solution for a binary tree in python.

class Node:

	#Construct new node with a key and child nodes
	def __init__(self, key):
	    self.key = key
	    self.left = None
	    self.right = None


# Gets path from tree root to given node
# Stores path in path[]
# Returns false if no path found
def getPath(root, path, k):
	if root is None:
		return False

	path.append(root.key)

	if root.key == k:
		return True

	if((root.left != None and getPath(root.left, path, k)) or 
		(root.right != None and getPath(root.right, path, k))):
		return True
	
	path.pop()
	return False

# Returns lowest common ancestor of nodeA and nodeB
# Returns -1 if node isnt present in tree
def getLCA(root, nodeA, nodeB):
	path1 = []
	path2 = []

	if(not getPath(root, path1, nodeA) or not getPath(root, path2, nodeB)):
		return -1

	i=0
	while (i<len(path1) and i < len(path2)):
		if path1[i] != path2[i]:
			break
		i+=1

	return path1[i-1]


root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(3)
root.left.right = Node(11)
root.right.right = Node(6)
root.right.left = Node(7)
		