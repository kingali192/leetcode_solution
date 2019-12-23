"""
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
    def lowestCommonAncestor_iterative(self, root, p, q):
        # Iterative Solution
        """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if p == q:
        return p
    if not root or not p or not q:
        return None
    min_val = min(p.val, q.val)
    max_val = max(p.val, q.val)
    
    curr = root
    while curr:
        if curr.val>=min_val and curr.val<=max_val:
            return curr
        elif curr.val<min_val and curr.val<max_val:
            curr = curr.right
        elif curr.val>min_val and curr.val>max_val:
            curr = curr.left
            
    return None