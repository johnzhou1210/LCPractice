def get_key_needed_to_increment_and_decrement(map1, map2):
    # iterate through map1 to check ones to increment
    # print(map1,map2)
    keyToIncrement = None
    for k,v in map1.items():
        if not k in map2:
            keyToIncrement = k
            break;
        if map2[k] < v:
            keyToIncrement = k
            break;
    # iterate through map2 to check ones to decrement
    keyToDecrement = None
    for k,v in map2.items():
        if not k in map1:
            keyToDecrement = k
            break;
        if map1[k] < v:
            keyToDecrement = k
            break;
    return keyToIncrement, keyToDecrement


def bow(str):
    result = dict()
    for char in str:
        result[char] = 1 if not char in result else result[char] + 1
    return result


def min_steps_to_match_maps(map1, map2):
    # f("bab","aba")
    # ['b':2, 'a':1] ['b':1, 'a':2]
    # In each step, if both dictionaries are identical, return current step.
    # In one step, decrement one key value and increment one key value of map2
    # If decrement results in zero, remove key.
    # Assuem that map1 and map2 are of equal length

    # get dictionary forms of map1 and map2
    d1 = bow(map1)
    d2 = bow(map2)

    match = False
    steps = 0
    while not match:
        if d1 == d2:
            match = True
            break
        # get keys to increment and decrement
        keyToIncrement, keyToDecrement = get_key_needed_to_increment_and_decrement(d1, d2)
        d2[keyToIncrement] = 1 if not keyToIncrement in d2 else d2[keyToIncrement] + 1
        d2[keyToDecrement] -= 1
        if d2[keyToDecrement] == 0:
            del d2[keyToDecrement]
        steps += 1
        
    return steps
   

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
print(min_steps_to_match_maps("onlytwentycharacters", "thisisatoughtestcase"))
print(min_steps_to_match_maps("",""))