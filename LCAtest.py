import LCA
import unittest

class testLCA(unittest.TestCase):

		#		     1
		#           /  \
		#	       /    \
		#         2      4
		#        / \    /  \
		#       3  11  7    6

	def test3_11(self):
		self.assertEqual(2, LCA.getLCA(LCA.root, 3, 11, ))

	def test2_11(self):
		self.assertEqual(2, LCA.getLCA(LCA.root, 2, 11, ))

	def test7_11(self):
		self.assertEqual(1, LCA.getLCA(LCA.root, 7, 11, ))

	def test3_4(self):
		self.assertEqual(1, LCA.getLCA(LCA.root, 3, 4, ))

	def test3_14(self):
		self.assertEqual(-1, LCA.getLCA(LCA.root, 3, 14, ))

	def testEmpty(self):
		self.assertEqual(-1, LCA.getLCA(None, None, None, ))


 
if __name__ == '__main__':
    unittest.main()