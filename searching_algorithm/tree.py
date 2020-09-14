# 木構造の中のノードを定義（ノードは値・左に子ノード、右に子ノードを持つ）
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
# 二分木クラスを定義
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    # 行きがけ順（preorder）を二分木クラスのメソッドとして生成
    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

# 二分木を作る
tree = BinaryTree(9)
tree.root.left = Node(3)
tree.root.right = Node(14)
tree.root.left.left = Node(1)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(4)
tree.root.left.right.right = Node(7)
tree.root.right.left = Node(12)
tree.root.right.right = Node(17)

# 定義した二分木を行きがけ順で出力
print(tree.preorder_print(tree.root, ''))