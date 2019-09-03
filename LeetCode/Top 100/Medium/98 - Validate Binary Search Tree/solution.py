# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
        
#         def recurse(currNode, valid):
#             if currNode == None:
#                 return True
            
#             val = currNode.val
#             print(val)
#             left = None
#             right = None
            
#             if currNode.left:
#                 left = currNode.left
#             if currNode.right:
#                 right = currNode.right
                
#             if left and right:
#                 if left.val < val and right.val > val:
#                     valid = recurse(left, valid)
#                     if valid:
#                         valid = recurse(right, valid)
#                 else:
#                     return False
#             elif left:
#                 if left.val < val:
#                     valid = recurse(left, valid)
#                 else:
#                     return False
#             elif right:
#                 if right.val > val:
#                     valid = recurse(right, valid)
#                 else:
#                     return False
#             return valid
        
#         isValid = True
#         isValid = recurse(root, isValid)
        
#         return isValid
            
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            print("NODE: " + str(node.val))
            print("LOWER: " + str(lower))
            print("UPPER: " + str(upper))
            print()
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)