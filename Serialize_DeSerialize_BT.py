# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return []
        res = []
        res.append(None)
        q  = list()
        q.append(root)
        while(len(q)>0):
            a = q.pop(0)
            res.append(a.val if a is not None else None)
            if a==None:
                continue
            q.append(a.left)
            q.append(a.right)

        for i in range(len(res)-1,0,-1):
            if res[i]==None:
                res.pop(i)
            else:
                break

        return str(res)


    def deserialize_helper(self,root,i,res):
        if root == None:
            return
        root.left = TreeNode(res[2*i])
        root.right = TreeNode(res[2*i + 1])
        self.deserialize_helper(root.left,2*i,res)
        self.deserialize_helper(root.right,2*i + 1,res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = eval(data)
        if(len(res)==0):
            return []
        root = TreeNode(res[1])
        res = self.deserialize_helper(root,1,res)
        return res







# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))