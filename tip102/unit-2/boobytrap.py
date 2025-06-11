def is_balanced(code):
    # Generate bag
    bow = dict()
    for char in code:
        bow[char] = 1 if not char in bow else bow[char] + 1
    
    # do a pass to check if all frequencies are equal first, and allow only one violation.
    # when violation found, record index.
    violationIndex = -1

    frequencySet = set()

    for k,v in bow.items():
        frequencySet.add(v)

    # return false if set length is greater than or equal to 3 (>= 2 violations)
    if len(frequencySet) >= 3:
        return False

    # if no violation, return false
    if len(frequencySet) == 1:
        return False

    # Now there must be 2 items in the set at this point.
    item1 = frequencySet.pop()
    item2 = frequencySet.pop()

    # return if absolute value of difference is equal to 1.
    return abs(item1 - item2) == 1

code1 = "arghh"
code2 = "haha"
code3 = "ggsdsmmdd"
code4 = "thisworkstrustme"

print(is_balanced(code1)) 
print(is_balanced(code2)) 
print(is_balanced(code3))
print(is_balanced(code4))