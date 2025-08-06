'''
Problem 1: Merging Cookie Orders

You run a local bakery and are given the roots of two binary trees order1 and order2 where each node in the binary tree 
represents the number of a certain cookie type the customer has ordered. To maximize efficiency, you want to bake enough 
of each type of cookie for both orders together.

Given order1 and order2, merge the order together into one tree and return the root of the merged tree. To merge the orders,
 imagine that when place one tree on top of the other, some nodes of the two trees are overlapped while others are not. 
 If two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the not None node will be used 
 as the node of the new tree.

Start the merging process from the root of both orders.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you 
believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    pass

Example Usage:

Example 'order1' and 'order2' trees and their merged result

"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))

Example Usage:

[3, 4, 5, 5, 4, None, 7]
Explanation:
Merged Tree:
     3
    /  \      
  4     5  
 / \      ''
5   4      7

'''
from collections import deque

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

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right
#U: Idea is to add the values of both trees at the same index/root and return the root of that tree
#M: Traversal sub-problem
#P: 
def merge_orders(order1, order2):
    modified_root = order1

    def helper(o1, o2):
        if not o1 and not o2:
            return
        # base case: if only order1 node exists
        if not o2:
            return o1
        # base case: if only order2 node exists
        if not o1:
            return o2
        
        o1.val = o1.val + o2.val
        o1.left = helper(o1.left, o2.left)
        o1.right = helper(o1.right, o2.right)

        return o1

    helper(order1, order2)

    return modified_root




    
def traversal(root, first_tree):
    if root is None:
       
       return root
    
    first_tree.append(root.val)

    traversal(root.left, first_tree)
    traversal(root.right, first_tree)

    return first_tree


    #result = []
    #first_tree = []
    #second_tree = []




cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

tree = []

# print_tree(merge_orders(order1, order2))



'''
Problem 2: Croquembouche

You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, that prints a list of the flavors (vals) of each cream puff in level order (i.e., from left to right, level by level).

Note: The build_tree() and print_tree() functions both use variations of a level order traversal. To get the most out of this problem, we recommend that you reference these functions as little as possible while implementing your solution.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    pass

Example Usage:

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche)

Example Output:

['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']

[, , , 'Matcha', 'Vanilla', 'Chocolate', 'Strawberry','Chocolate','Vanilla','Matcha','Strawberry','Vanilla']



'''

# do a BFS traversal
# Intuition: push nodes down a queue if any node has children so they will be accessed later to favor nodes at the tree's current level
from collections import deque
def print_design(design):
    if not design:
        print("[]")
        return
    result = []
    queue = deque([design])
    while queue:
        front = queue.popleft()
        result.append(front.val)
        if front.left:
            queue.append(front.left)
        if front.right:
            queue.append(front.right)
    print(result)

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
# print_design(croquembouche)


'''
Problem 3: Maximum Tiers in Cake

You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake, where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different section of your cake, return the maximum number of tiers in your cake.

The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
'''

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if not cake:
        return 0
    return 1 + max(max_tiers(cake.left), max_tiers(cake.right))

def max_tiers_bfs(cake):
    if not cake:
        return 0
    result = 0
    queue = deque([cake])
    while (queue):
        for i in range(0,len(queue)):
            front = queue.popleft()
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
        result += 1
    return result


"""
Example Usage:

        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee

Example Output:

3
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

# print(max_tiers(cake))
# print(max_tiers_bfs(cake))



'''
Problem 5: Can Fulfill Order

At your bakery, you organize your current stock of baked goods in a binary tree with root inventory where each node represents the quantity of a baked good in your bakery. A customer comes in wanting a random assortment of baked goods of quantity order_size. Given the root inventory and integer order_size, return True if you can fulfill the order and False otherwise. You can fulfill the order if the tree has a root-to-leaf path such that adding up all the values along the path equals order_size.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
'''


class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def can_fulfill_order(inventory, order_size):
    if not inventory:
        return False
    if order_size < 0:
        return False
    if not inventory.left and not inventory.right:
        return order_size == inventory.val
    return can_fulfill_order(inventory.left, order_size - inventory.val) or can_fulfill_order(inventory.right, order_size - inventory.val)

"""
Example Usage:


             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   

Example Output:

True
Example 1 Explanation: 5 + 4 + 11 + 2 = 22

False
"""

# Using build_tree() function included at top of the page
quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

# print(can_fulfill_order(baked_goods, 22))
# print(can_fulfill_order(baked_goods, 2))


'''
Problem 6: Icing Cupcakes in Zigzag Order

You have rows of cupcakes represented as a binary tree cupcakes where each node in the tree represents a cupcake. To ice them efficiently, you are icing cupcakes one row (level) at a time, in zig zag order (i.e., from left to right, then right to left for the next row and alternate between).

Return a list of the cupcake values in the order you iced them.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right



Example Usage:

"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   

Using build_tree() function included at top of page

Example Output:

['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
"""

'''

def zigzag_icing_order(cupcakes):
    # dfs: if current level is even/odd, do a pop or popleft
    if not cupcakes:
        return []
    result = []
    queue = deque([cupcakes])
    level = 0
    while queue:
        level_len = len(queue)
        for i in range(0,level_len):
            popped = queue.popleft() if level % 2 == 0 else queue.pop()
            result.append(popped.val)
            if level % 2 == 0:
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            else:
                if popped.left:
                    queue.appendleft(popped.left)
                if popped.right:
                    queue.appendleft(popped.right)

        level += 1
    return result

flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))