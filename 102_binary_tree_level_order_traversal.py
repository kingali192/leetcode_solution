"""
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7]
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans, level = [], [root]
        while level: # while going through levels of root
            ans.append([node.val for node in level]) # append node values at that level
            temp = []
            for node in level: #for each node at level
                temp.extend([node.left, node.right]) # make sure to [have left values and right values at that level]
            level = [leaf for leaf in temp if leaf] # don't know!
        return ans