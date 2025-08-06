def is_profitable(excursion_costs):
    # Time complexity: O(n)
    # Space complexity: O(1)
    # I don't think this is what the question was asking...

    num_excursions = len(excursion_costs)
    smallest_excursion = min(excursion_costs)
    x = num_excursions if num_excursions < smallest_excursion else smallest_excursion

    if smallest_excursion < x:
        return -1
    if num_excursions > x:
        return -1
    return x

print(is_profitable([3, 5]))
print(is_profitable([0, 0]))
