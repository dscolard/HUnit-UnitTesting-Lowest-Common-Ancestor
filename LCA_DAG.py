

class Node:

    def __init__(self, key):
        self.key = key
        self.pred = []
        self.succ = []

def getLCA(root, n1, n2):

    if root is None:
            return None

    if root == n1 or root == n2:
        return root.key

    i=0
    lca = []

    while(i < len(n1.pred)):
        j=0
        while(j<len(n2.pred)):

            if(n1.pred[i].key == n2.pred[j].key):
                lca.append(n1.pred[i].key)
                j+=1
            else:
                j+=1
        i+=1
    if lca:
        # Return lowest common ancestor
        return max(lca)
    
    return root.key

# Create Nodes
root = Node(1)
r2 = Node(2)
r3 = Node(3)
r4 = Node(4)
r5 = Node(5)
r6 = Node(6)

# Create DAG
root.succ = [r2,r3,r4,r5]
r2.succ = [r6]
r2.pred = [r2, root]
r3.succ = [r5]
r3.pred = [r3, root, r6]
r4.pred = [r4, root, r6]
r5.succ = [r6]
r5.pred = [r5, r3, root]
r6.succ = [r3]
r6.pred = [r6, r2, r5, r4]