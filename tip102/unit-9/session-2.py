'''
Problem 1: Haunted Mirror

A vampire has come to stay at the haunted hotel, but he can't see his reflection! What's more, he doesn't seem to be able to see the reflection of anything in the mirror! He's asked you to come to his aid and help him see the reflections of different thngs.

Given the root of a binary tree vampire, return the mirror image of the tree. The mirror image of a tree is obtained by flipping the tree along its vertical axis, meaning that the left and right children of all non-leaf nodes are swapped.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
'''
'''


"""
      🧛‍♂️
     /   \
    💪🏼    🤳
    /      \
   👟       👞
"""
# Using build_tree() function included at the top of the page
body_parts = ["🧛‍♂️", "💪🏼", "🤳", "👟", None, None, "👞"]
vampire = build_tree(body_parts)


"""
      🎃
     /   \
    😈    🕸️
         /  \
       🧟‍♂️    👻
"""
spooky_objects = ["🎃", "😈", "🕸️", None, None, "🧟‍♂️", "👻"]
spooky_tree = build_tree(spooky_objects)

# Using print_tree() function included at the top of the page
print_tree(mirror_tree(vampire))
print_tree(mirror_tree(spooky_tree)) 

Example Output:

['🧛‍♂️', '🤳', '💪🏼', '👞', None, None, '👟']
Example 1 Explanation:
Mirrored Tree:
      🧛‍♂️
    /    \
  🤳     💪🏼
 /         \
👞          👟

['🎃', '🕸️', '😈', '👻', '🧟‍♂️',]
Example 2 Explanation:
Mirrored Tree:
      🎃
    /    \
  🕸️     😈
 /  \
👻  🧟‍♂️

'''

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def mirror_tree(root):
    if not root:
        return root
    temp = root.left
    root.left = mirror_tree(root.right)
    root.right = mirror_tree(temp)
    return root

"""
      🧛‍♂️
     /   \
    💪🏼    🤳
    /      \
   👟       👞
"""
# Using build_tree() function included at the top of the page
body_parts = ["🧛‍♂️", "💪🏼", "🤳", "👟", None, None, "👞"]
vampire = build_tree(body_parts)


"""
      🎃
     /   \
    😈    🕸️
         /  \
       🧟‍♂️    👻
"""
spooky_objects = ["🎃", "😈", "🕸️", None, None, "🧟‍♂️", "👻"]
spooky_tree = build_tree(spooky_objects)

# Using print_tree() function included at the top of the page
print_tree(mirror_tree(vampire))
print_tree(mirror_tree(spooky_tree)) 