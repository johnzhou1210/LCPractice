def get_item(items, x):
    if x >= 0 and x < len(items):
        return items[x]
    return None
    

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))
