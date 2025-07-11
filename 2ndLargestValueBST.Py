class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Insert node into BST
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Find 2nd largest using reverse in-order traversal
def find_second_largest(root):
    count = [0]
    result = [None]

    def reverse_in_order(node):
        if node is None or count[0] >= 2:
            return
        reverse_in_order(node.right)
        count[0] += 1
        if count[0] == 2:
            result[0] = node.val
            return
        reverse_in_order(node.left)

    reverse_in_order(root)
    return result[0]

# ---------- Input Section ----------
try:
    user_input = input("Enter elements of BST separated by space: ")
    elements = list(map(int, user_input.strip().split()))

    if len(elements) < 2:
        print("At least two nodes are required in the BST.")
    else:
        root = None
        for val in elements:
            root = insert(root, val)

        second_largest = find_second_largest(root)
        if second_largest is not None:
            print("Second largest element in the BST is:", second_largest)
        else:
            print("Could not find second largest (tree may have only one unique element).")

except ValueError:
    print("Invalid input. Please enter integers only.")