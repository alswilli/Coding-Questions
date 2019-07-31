# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t3 = None
        t3 = self.traverse(t1, t2, t3)
        return t3
        
    def traverse(self, t1, t2, t3):
        if t1 == None and t2 == None:
            return None
        if t1 != None and t2 == None:
            t3 = TreeNode(t1.val)
            t3.left = self.traverse(t1.left, t2, t3.left)
            t3.right = self.traverse(t1.right, t2, t3.right) 
        if t1 == None and t2 != None:
            t3 = TreeNode(t2.val)
            t3.left = self.traverse(t1, t2.left, t3.left)
            t3.right = self.traverse(t1, t2.right, t3.right) 
        if t1 != None and t2 != None:
            t3 = TreeNode(t1.val + t2.val)
            t3.left = self.traverse(t1.left, t2.left, t3.left)
            t3.right = self.traverse(t1.right, t2.right, t3.right)
        return t3