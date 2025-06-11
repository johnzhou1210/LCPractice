def find_treasure_indices(gold_amounts, target):
    # problem looks like two-sum
    wantedNumbers = dict()
    for i,v in enumerate(gold_amounts):
        wantedNumbers[target - v] = i

    # exmaple: [2,7,11,15]
    # wanted numbers: [7:0, 2:1, -2:2, -6:3]

    for i,v in enumerate(gold_amounts):
        if v in wantedNumbers and wantedNumbers[v] != i:
            return [i,wantedNumbers[v]]
    return [0,0]
    
    
    
gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

gold_amounts4 = [3, 3,7,11,3,-4]
target4 = 10


print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  
print(find_treasure_indices(gold_amounts4, target4))  