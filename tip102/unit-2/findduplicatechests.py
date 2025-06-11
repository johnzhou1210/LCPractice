def find_duplicate_chests(chests):
    freqMap = dict()
    for _,v in enumerate(chests):
        freqMap[v] = 1 if not v in freqMap else freqMap[v] +1
    result = []
    for k,v in freqMap.items():
        if v == 2:
            result.append(k)
    return result


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
