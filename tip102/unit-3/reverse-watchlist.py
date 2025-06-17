# We want to reverse an array in place with two-pointer approach

# e.g. [2,4,7,5,1,8]
# [8,4,7,5,1,2] # First iteration
# [8,1,7,5,4,2] # Second iteration
# [8,1,5,7,4,2] # Third iteration
# Fourth iteration: pointer_1 should be greater than or equal to pointer_2 index

def reverse_watchlist(watchlist):
# 1. Intialize pointer_1 and pointer_2
    # a. pointer_1 starts at index 0
    pointer_1 = 0
    # b. pointer_2 starts at index len(arr) - 1
    pointer_2 = len(watchlist) - 1

# 2. While pointer_1's index is less than pointer_2's index:
    while pointer_1 < pointer_2:
        # a. Swap the values of pointer_1 and pointer_2
        #   i. Use a temporary variable to store value of pointer_1 so we don't lose the original value
        temp = watchlist[pointer_1]
        watchlist[pointer_1] = watchlist[pointer_2]
        watchlist[pointer_2] = temp
        # b. Increment pointer_1, decrement pointer_2
        pointer_1 += 1
        pointer_2 -= 1
    # 3. Return the array
    return watchlist


watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]
watchlist2 = ["Breaking Bad"]
watchlist3 = ["Breaking Bad", "The Crown", "The Witcher"]
watchlist4 = []

print(reverse_watchlist(watchlist))
print(reverse_watchlist(watchlist2))
print(reverse_watchlist(watchlist3))  
print(reverse_watchlist(watchlist4))  