# Combine list items into dictionary, assuming that both lists are the same size

def lineup(artists, set_times):
    # 1. Create dictionary
    dictionary = {}
    # 2. Iterate through the artists list
    for i in range(0, len(artists), 1):
        #   a. Add a key value pair to dictionary (artist, set time)
        dictionary[artists[i]] = set_times[i]
        #   b. artist[i] and set_times[i]
    # return dictionary
    return dictionary

# Edge cases
# All accounted for?
# 

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

artists3 = ["john$!@$","!@$(^^$#)","!@$*#!$%()$@!#"]
set_times3 = ["9:@!$!30 PM","2:35 PM", "6:00PM"]

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
print(lineup(artists3, set_times3))