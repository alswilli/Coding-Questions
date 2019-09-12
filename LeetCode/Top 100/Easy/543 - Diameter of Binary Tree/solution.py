# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         def recurse(rootNode, sum = 0, best = 1):
#             if rootNode == None:
#                 return 0
#             else: #there is a Node
#                 # sum += 1 
#                 bestLeft = recurse(rootNode.left, sum+1, best)
#                 print("LEFT: " + str(bestLeft))
#                 bestRight = recurse(rootNode.right, sum+1, best)
#                 print("RIGHT: " + str(bestRight))
#                 best = max(best, bestLeft +  bestRight)
#                 return max(bestLeft, bestRight)
        
#         count = 0
#         count = recurse(root)
#         return count
    
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1