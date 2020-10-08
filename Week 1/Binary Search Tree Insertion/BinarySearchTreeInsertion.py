
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Average Time Complexity: O(logn)
# Average Space Complexity: O(logn)
# Worst Time Complexity: O(n)
# Worst Space Complexity: O(n)


def insertIntoBST(root, val):
    if root is None:
        root = TreeNode(val)
    else:
        current = root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                else:
                    current = current.right
        return root
