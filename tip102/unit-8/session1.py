'''
Problem 1: Grafting Apples

You are grafting different varieties of apple onto the same root tree can produce 
many different varieties of apples! Given the following TreeNode class, create the 
binary tree depicted below. The text representing each node should should be used as the value.

The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.

             Trunk
          /         \
      Mcintosh   Granny Smith
      /     \       /     \
    Fuji   Opal   Crab   Gala

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk")

Example Usage:

# Using print_tree() included at the top of this page
print_tree(root)

Example Output:

['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']

'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

from collections import deque
def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# root = TreeNode("Trunk")
# root.left = TreeNode("Mcintosh")
# root.right = TreeNode("Granny Smith")
# root.left.left = TreeNode("Fuji")
# root.left.right = TreeNode("Opal")
# root.right.left = TreeNode("Crab")
# root.right.right = TreeNode("Gala")

# print_tree(root)

'''
Problem 2: Calculating Yield

You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

    Leaf nodes have an integer value.
    The root has a string value of either "+", "-", "*", or "-".

The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  pass

Example Usage:

"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))

Example Output:

12
'''

def calculate_yield(root):
    if root.val == "+":
        return root.left.val + root.right.val
    elif root.val == "-":
        return root.left.val - root.right.val
    elif root.val == "*":
        return root.left.val * root.right.val
    elif root.val == "/":
        return root.left.val / root.right.val
    return

# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
# apple_tree2 = TreeNode("-", TreeNode(7), TreeNode(5))
# apple_tree3 = TreeNode("*", TreeNode(7), TreeNode(5))
# apple_tree4 = TreeNode("/", TreeNode(7), TreeNode(5))
# print(calculate_yield(apple_tree))
# print(calculate_yield(apple_tree2))
# print(calculate_yield(apple_tree3))
# print(calculate_yield(apple_tree4))


'''
Problem 3: Ivy Cutting

You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
  pass

Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))

Example Output:

['Root', 'Node2', 'Leaf3']
['Root']
'''

def right_vine(node):
    # just remove the left child to get the right vine
    node.left = None
    return node

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print_tree(right_vine(ivy1))
# print_tree(right_vine(ivy2))

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# oak1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(count_leaves(oak1))
# print(count_leaves(oak2))

def survey_tree(root):
    def helper(curr, result):
        if not curr:
            return
        helper(curr.left, result)
        helper(curr.right, result)
        result.append(curr.val)
    result = []
    helper(root, result)
    return result

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

def harvest_berries(root, threshold):
    if not root:
        return 0
    return (root.val if root.val > threshold else 0) + harvest_berries(root.left, threshold) + harvest_berries(root.right, threshold)

# """
#        4
#      /   \
#    10     6
#   /  \     \
#  5    8    20
# """
# bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

# print(harvest_berries(bush, 6))
# print(harvest_berries(bush, 30))


def find_flower(root, flower):
  if not root:
      return False
  return root.val == flower or find_flower(root.left, flower) or find_flower(root.right, flower)


"""
         Rose
        /    \
       /      \
     Lily     Daisy
    /    \        \
Orchid  Lilac    Dahlia
"""

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))
