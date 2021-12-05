# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedHelper(self, root):
        if root == None:
            return 1,0
        if root.left == None and root.right == None:
            return 1,1
        l_b,l_h = self.isBalancedHelper(root.left)
        r_b,r_h = self.isBalancedHelper(root.right)
        if(l_b==0 or r_b==0):
            return 0,max(l_h,r_h)+1
        if(abs(r_h-l_h)>1):
            return 0,max(l_h,r_h)+1
        else:
            return 1,max(l_h,r_h)+1

    def isBalanced(self, root):
        x,_ = self.isBalancedHelper(root)
        if x==1:
            return True
        else:
            return False
        