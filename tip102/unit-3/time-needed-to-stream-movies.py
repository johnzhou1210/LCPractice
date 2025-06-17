# Plan:
# use one pointer
# steps = 0
# while pointer not at end:
#   if curr item > 0: decrement curr item and increment steps
#   if curr item == 0 and pointer == k: return steps
#   increment pointer
#   if pointer at end: pointer = 0
# return steps

def time_required_to_stream(movies, k):
    steps = 0
    # edge case: the user in question does not have any movies to stream to begin with
    if movies[k] <= 0:
        return steps

    ptr = 0
    while ptr < len(movies):
        if movies[ptr] > 0:
            movies[ptr] -= 1
            steps += 1
        if movies[ptr] == 0 and ptr == k:
            return steps
        ptr += 1
        if ptr == len(movies):
            ptr = 0
    return steps



print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0)) 