import math

def split_list(list, chunk_size):
    return [list[i:i+chunk_size] for i in range(0, len(list), chunk_size)]

def split_list2(list, chunk_size):
    result = []
    for i in range(0, len(list), chunk_size):
        result.append(list[i:i+chunk_size])
    return result

def organize_pirate_crew(group_sizes):
    # first see how many groups of each size we will need.
    groupsTally = dict() # Keeps track of each group type, and the indices in each group

    for i,v in enumerate(group_sizes):
        if not v in groupsTally:
            groupsTally[v] = [i]
        else:
            groupsTally[v].append(i)
    
    # Example: [3,3,3,3,3,1,3]
    # groupsTally = [3:[0,1,2,3,4,6], 1:[5]]
    # split_list([0,1,2,3,4,6],3) => [[0,1,2],[3,4,6]]

    # Go through each dictionary item and split them
    result = []
    for k,v in groupsTally.items():
        itemsToAppend = split_list2(v,k)
        for item in itemsToAppend:
            result.append(item)
    
    return result
    






group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 
print(organize_pirate_crew([1,2,2,1,2,1,2]))