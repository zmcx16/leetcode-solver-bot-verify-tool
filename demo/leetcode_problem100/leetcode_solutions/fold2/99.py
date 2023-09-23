class Solution:
    def recoverTree(self, root):
        stack = []
        prev = None
        curr = root
        nodes_to_swap = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and prev.val > curr.val:
                nodes_to_swap.append(prev)
                nodes_to_swap.append(curr)
            prev = curr
            curr = curr.right
        nodes_to_swap[0].val, nodes_to_swap[1].val = nodes_to_swap[1].val, nodes_to_swap[0].val