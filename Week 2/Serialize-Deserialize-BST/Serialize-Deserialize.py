class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)


class Codec:
    def serialize(self, root):
        def postorder(root):
            if not root:
                return []
            return postorder(root.left) + postorder(root.right) + [root.val]
        return " ".join(map(str, postorder(root)))

    def deserialize(self, data):
        def helper(lower=float("-inf"), upper=float("inf")):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root
        data = [int(x) for x in data.split(" ") if x]
        return helper()


root = TreeNode(8)
root.left = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(7)
root.right = TreeNode(10)

codec = Codec()
values = codec.serialize(root)
print(values)

newRoot = codec.deserialize(values)
values = codec.serialize(newRoot)
print("*****")
print(values)
