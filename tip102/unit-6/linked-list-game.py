class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next



def game_result(head):
    # Plan
    # Assume list is of even length
    # 1. Handle edge case of list is empty -> return "Tie"
    if head == None:
        return "Tie"
    even_score = 0
    odd_score = 0
    # 2. Iterate through linked list, two nodes at a time.
    left = head
    right = head.next
    while right != None:
		#   a. If left node is greater, grant point to even
        if left.value > right.value:
            even_score += 1
		#   b. Else if right node is greater, grant point to odd
        elif right.value > left.value:
            odd_score += 1
        #   c. Else (if equal), grant points to both even and odd or not at all (shouldn't affect outcome)
        else:
            even_score += 1
            odd_score += 1
        
        left = left.next
        if right.next == None:
             break
        right = right.next.next
  
    # return "Odd" if odd is greater than even, "Even" if even is greater than odd, and "Tie" if equal.
    if even_score == odd_score:
        return "Tie"
    return "Odd" if odd_score > even_score else "Even"
	




game1 = Node(2, Node(1))
game2 = Node(2, Node(5, Node(4, Node(7, Node(20, Node(5))))))
game3 = Node(4, Node(5, Node(2, Node(1))))
game4 = None

print(game_result(game1))
print(game_result(game2))
print(game_result(game3))
print(game_result(game4))