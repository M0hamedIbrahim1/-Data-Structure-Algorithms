# link : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# author : Mohamed Ibrahim


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(root):
            if not root:
                res.append('N')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)
    def deserialize(self, data):
        res = data.split(',')
        self.i = 0
        def dfs():
            if res[self.i] == 'N':
                self.i+=1
                return None
            node = TreeNode(int(res[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

