import json


class Solution:
    def inorderTraversal(self, root):
        def inorder(node, res):
            if node is None:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
        res = []
        inorder(root, res)
        return json.dumps(res)