"""
98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        def inorder(root, result):
            if root:
                inorder(root.left, result)
                result.append(root.val)
                inorder(root.right, result)
        
        inorder(root, result)
    
        return sorted(list(set(result))) == result # if the results you generated through inorder traversal is teh same as it's sorted version in a list true!