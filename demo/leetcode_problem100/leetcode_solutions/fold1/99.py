def recoverTree(self, root: Optional[TreeNode]) -> None:
    def inorder(node):
        nonlocal prev, first, second
        if node is None:
            return
        inorder(node.left)
        if prev and prev.val > node.val:
            if first is None:
                first = prev
            second = node
        prev = node
        inorder(node.right)
    prev = first = second = None
    inorder(root)
    first.val, second.val = second.val, first.val