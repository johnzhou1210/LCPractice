class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
    # Plan
    # 1. Keep track of previously visited nodes in a set
    visited = set()
    # 2. Iterate through linked list.
    curr_node = path_start
    while curr_node != None:
        #   a. Add the current node to the set
        visited.add(curr_node)
        #   b. If current node's next is in set, return current node.
        if curr_node.next != None and curr_node.next in visited:
            return curr_node.next
        #   c. Increment current node
        curr_node = curr_node.next
    # 3. Return None if outside of loop
    return None


path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next

result = cycle_start(path_start)

print(result if result == None else result.value )