# "abbaca" -> "aaca" -> "ca"
# a -> ab -> a -> (empty) -> c -> ca

# Plan:
# 1. Create an empty stack that will store result
# 2. Iterate through the schedule string, no need to keep track of index
#   a. If stack is empty, push current character to stack
#   b. Otherwise, if top of stack is the same as the current character, pop the stack.
#   c. Else, push the current character to stack.
# 3. Return the stack after converting it to a string.
#   a. We will need another stack as a temporary stack so we can reverse the stack to ensure proper order.
#   b. e.g. [ca] [] -> [c] [a] -> [][ac]  
#   c. while stack1 is not empty: pop item from stack1 and push into stack2.
#   d. create an empty string variable holding the result
#   e. while stack2 is not empty: pop item from stack2 and concat into result string.
#   f. return result string

# Edge cases:
# 1. Stack is empty

def remove_duplicate_shows(schedule):
    stack = []
    for char in schedule:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    temp_stack = []
    while len(stack) > 0:
        popped_item = stack.pop()
        temp_stack.append(popped_item)
    result = ""
    while len(temp_stack) > 0:
        popped_item = temp_stack.pop()
        result += popped_item
    return result
    


print(remove_duplicate_shows("abbaca")) 
print(remove_duplicate_shows("azxxzy")) 
print(remove_duplicate_shows("")) 
print(remove_duplicate_shows("yyyyyyy"))
print(remove_duplicate_shows("hhhhhh"))
print(remove_duplicate_shows("b")) 