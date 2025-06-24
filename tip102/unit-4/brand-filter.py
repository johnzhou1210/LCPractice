# plan
# 1. Create result list to store result
# 2. Iterate through brands (list of dictionaries)
#   a. For each brand, iterate through criteria list
#       i. If criterion found, add brand name to result list and break from criteria iteration loop.
# 3. Return result list

# edge cases
# 1. Criteria is not found: just don't add the brand name
# 2. Case sensitivity? Ignore it.

def filter_sustainable_brands(brands, criterion):
    result = []
    for brand in brands:
        for desc in brand["criteria"]:
            if desc == criterion:
                result.append(brand["name"])
                break
    return result


brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))
