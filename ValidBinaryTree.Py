class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    
    if not (min_val < root.val < max_val):
        return False
    
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))

# ----------- Example Binary Tree -----------

# Constructing this tree:
#        10
#       /  \
#      5    15
#          /  \
#         12   20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# ----------- Validation -----------
if is_valid_bst(root):
    print("The tree is a valid Binary Search Tree.")
else:
    print("The tree is NOT a valid Binary Search Tree.")