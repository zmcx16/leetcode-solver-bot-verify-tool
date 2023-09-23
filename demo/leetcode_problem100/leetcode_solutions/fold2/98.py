def isValidBST(self, root: Optional[TreeNode]) -> bool:
    stack = []
    prev_value = float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= prev_value:
            return False
        prev_value = root.val
        root = root.right
    return True