import unittest
import LCA_DAG

class TestLca(unittest.TestCase):

    def test_node1_3(self):
        self.assertEqual(LCA_DAG.getLCA(LCA_DAG.root, LCA_DAG.root, LCA_DAG.r3), 1)

    def test_node_None(self):
        self.assertEqual(LCA_DAG.getLCA(None, 1, 3), None)

    def test_node6_5(self):
        self.assertEqual(LCA_DAG.getLCA(LCA_DAG.root, LCA_DAG.r6, LCA_DAG.r5), 5)

    def test_node2_3(self):
        self.assertEqual(LCA_DAG.getLCA(LCA_DAG.root, LCA_DAG.r2, LCA_DAG.r3), 1)

    def test_node5_4(self):
        self.assertEqual(LCA_DAG.getLCA(LCA_DAG.root, LCA_DAG.r5, LCA_DAG.r4), 1)

    def test_node5_2(self):
        self.assertEqual(LCA_DAG.getLCA(LCA_DAG.root, LCA_DAG.r5, LCA_DAG.r2), 1)

    def test_node4_3(self):
        self.assertEqual(LCA_DAG.getLCA(LCA_DAG.root, LCA_DAG.r4, LCA_DAG.r3), 6)


if __name__ == '__main__':
    unittest.main()
