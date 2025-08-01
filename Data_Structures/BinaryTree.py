"""
 The keys in a binary search tree are always stored in such a way as to satisfy the
 binary-search-tree property:
    Let x be a node in a binary search tree. If y is a node in the left subtree of x, then y.key <= x.key. 
    If y is a node in the right subtree of x, then y.key >= x.key.
 
Types of Binary tree traversals:   
    1. Inorder walk prints the key of the self.root of a subtree between printing the values in its 
       left subtree and printing those in its right subtree (Left → self.root → Right)
       
    2. Preorder walk prints the self.root before the values in either subtree (self.root → Left → Right)
    
    3. Postorder walk prints the self.root after the values in its subtrees (Left → Right → self.root)

Types of Binary Tree based on the number of children:
    1. Full Binary Tree - A Binary Tree is a full binary tree if every node has 0 or 2 children.
    2. Degenerate (or pathological) Binery Tree - A Tree where every internal node has one child. 
       Such trees are performance-wise same as linked list. 
       A degenerate or pathological tree is a tree having a single child either left or right.
    3. Skewed Binary Tree - A skewed binary tree is a pathological/degenerate tree in which the tree is either dominated 
       by the left nodes or the right nodes. 
       Thus, there are two types of skewed binary tree: left-skewed binary tree and right-skewed binary tree.

Types of Binary Tree On the basis of the completion of levels:
    1. Complete Binary Tree - A Binary Tree is a Complete Binary Tree if all the levels are completely filled except possibly 
       the last level and the last level has all keys as left as possible. A complete binary tree is just like a full binary tree, 
       but with two major differences: 
            1. Every level except the last level must be completely filled.
            2. All the leaf elements must lean towards the left.
            3. The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.
    2. Perfect Binary Tree - A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all 
       leaf nodes are at the same level. The following are examples of Perfect Binary Trees. A perfect binary tree is a type of binary tree in 
       which every internal node has exactly two child nodes and all the leaf nodes are at the same level.
       In a Perfect Binary Tree, the number of leaf nodes is the number of internal nodes plus 1.
    3. Balanced Binary Tree - Provide O(log(n)) runtime complixity.
"""

class Node:
    def __init__(self, val="", left=None, right=None, ancestor=None):
        self.val = val
        self.left = left
        self.right = right
        self.ancestor = ancestor

class BinaryTree(object):
    def __init__(self):
        pass


    def inorder_traverse(self, root):
        if root is not None:    
            self.inorder_traverse(root.left)
            print(root.val)
            self.inorder_traverse(root.right)
        
            
    def preorder_traverse(self, root):
        if root is not None:    
            print(root.val)
            self.preorder_traverse(root.left)
            self.preorder_traverse(root.right)
        
            
    def postorder_traverse(self, root):
        if root is not None:    
            self.postorder_traverse(root.left)
            self.postorder_traverse(root.right)
            print(root.val)
        
            
    def search_tree(self, root, val):
        if root is None or root.val == val:
            return root
        if val < root.val:
            return self.search_tree(root.left, val)
        else:
            return self.search_tree(root.right, val)
        
        
    def find_maximum(self, root):
        while root:
            root = root.right
        return root


    def find_minimum(self, root):
        while root:
            root = root.left
        return root


    def find_successor(self, root):
        # Case 1. Given there is the right subtree
        if root.right:
            return self.find_minimum(root.right)
        # Case 2. Moving up the tree until we find the lowest ancestor of x that is a left child of its parent. 
        # The parent node will be the succesor of node x.
        curr = root
        parent = curr.ancestor
        while parent and parent.left != curr:
            curr = parent
            parent = parent.ancestor
            
        return parent
    
    
    def find_predecessor(self, root):
        # Case 1. Given there is the left subtree
        if root.left:
            return self.find_maximum(root.left)
        # Case 2. Moving up the tree until we find the lowest ancestor of x that is a right child of its parent. 
        # The parent node will be the succesor of node x.
        curr = root
        parent = curr.ancestor
        while parent and parent.right != curr:
            curr = parent
            parent = parent.ancestor
            
        return parent
    
    
    def insert_to_bst(self, root, node):
        if root is None:
            root = node
        
        curr = root
        parent = None # We need to keep this to be able to find a proper place for our node below
        while curr:
            parent = curr
            if node.val < curr.val:
                curr = curr.left
            else: 
                curr = curr.right
        
        node.ancestor = parent
        if node.val < parent.val:
            parent.left= node
        else: parent.right = node
        """
        Using Recursion
        
        if root is None:
            return node
        
        if node.key < root.key:
            root.left = self.insert_to_bst(root.left, node)
        else:
            root.right = self.insert_to_bst(root.left, node)
        
        return root
        """ 
        return root
    
    
    def __transplant(self, root, u, v):
        if u.ancestor is None:
            root = v        
        elif u.ancestor.left == u:
            u.ancestor.left = v
        else: u.ancestor.right = v
        
        if v:
            v.ancestor = u.ancestor
        return root
        
        
    def delete_from_bst(self, root, node):
        if root is None or node is None:
            print("[NO NODES IN THE TREE]")
            return root
        
        # If node z has only one child (right)
        if not node.left:
            root = self.__transplant(root, node, node.right)
        
        # If node z has only one child (left)
        elif not node.right:
            root = self.__transplant(root, node, node.left)
            
        # If node z has two children (right & left)
        else:
            # Find the successor of the right subtree
            # Find successor function requires O(h) runtime, where h = log(n), at worse case
            successor = self.find_minimum(node.right)
            if successor.ancestor != node:
                # Replace a subtree rooted at successor with successor.right (with right child of a successor)
                self.__transplant(root, successor, successor.right)
                
                successor.right = node.right
                if successor.right:
                    successor.right.ancestor = successor
        
            # Replace a subtree rooted at node with successor (successor now takes place of a deleted node 'node')
            self.__transplant(root, node, successor)
 
            # Pointer wrangling 
            successor.left = node.left
            if successor.left:
                node.left.ancestor = successor        
            
            """
              At this point we can remove (free memory) of node 'node'
              because it doesn't point to anything and is not pointed by anything
            """
        return root
            

tree = BinaryTree()

root = Node(50)
tree.insert_to_bst(root, Node(30))
tree.insert_to_bst(root, Node(70))
tree.insert_to_bst(root, Node(20))
tree.insert_to_bst(root, Node(40))
tree.insert_to_bst(root, Node(60))
tree.insert_to_bst(root, Node(80))

print("Inorder traversal before deletion:")
tree.inorder_traverse(root)

node_to_delete = tree.search_tree(root, 70)
root = tree.delete_from_bst(root, node_to_delete)

print("\nInorder traversal after deleting 70:")
tree.inorder_traverse(root)
