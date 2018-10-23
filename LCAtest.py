import LCA
import unittest

class testLCA(unittest.TestCase):

	def testTree(self):
		root = LCA.Node(1)
		root.left = LCA.Node(2)
		root.right = LCA.Node(4)
		root.left.left = LCA.Node(3)
		root.left.right = LCA.Node(11)
		root.right.right = LCA.Node(6)
		root.right.left = LCA.Node(7)

		#		     1
		#           /  \
		#	       /    \
		#         2      4
		#        / \    /  \
		#       3  11  7    6

		self.assertEqual(2, LCA.getLCA(root, 3, 11, ))
		self.assertEqual(2, LCA.getLCA(root, 2, 11, ))
		self.assertEqual(1, LCA.getLCA(root, 7, 11, ))
		self.assertEqual(1, LCA.getLCA(root, 3, 4, ))

		#Test unknown self
		self.assertEqual(-1, LCA.getLCA(root, 3, 14, ))


	def testEmpty(self):
		self.assertEqual(-1, LCA.getLCA(None, None, None, ))


 
if __name__ == '__main__':
    unittest.main()