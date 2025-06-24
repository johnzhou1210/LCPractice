# The plan
def is_valid_post_format(posts):
    # 1. Create a stack
    stack = []
    opening_chars = "([{"
    closing_chars = ")]}"

    # 2. Iterate through the posts string
    for char in posts:
        #   a. If the current character is one of the opening ones, push to stack.
        if char in opening_chars:
            stack.append(char)
        #   b. otherwise, if it is a closed one
        elif char in closing_chars:
            #       i. If stack empty, return False 
            if len(stack) == 0:
                return False
            #       ii. If the current character does not match the item on top of the stack, return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            if char == '}' and stack[-1] != '{':
                return False
            #       ii. Else, pop item at top of stack
            else:
                stack.pop()
    # 3. if stack empty, return True
    return len(stack) == 0

# Assuming that only input characters are ()[]{}
# "{(]}"
# {(
#  Edge cases: Unexpected input, empty string

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
print(is_valid_post_format("{({})([{}]){}}"))
print(is_valid_post_format(""))
