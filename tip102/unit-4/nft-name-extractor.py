# input: list of dictionaries

# Plan:
# 1. Create a variable to store the result list
# 2. Iterate through the input list
#   a. For each list item (dictionary), append the current dictionary["name"] value to result list
# 3. Return result list

# Edge cases:
# 1. Improperly formatted dictionary? (we assume name key exists)
#       How to handle? 
#           a. Ignore the nft all together and not add it to the returned list <- Let's handle it like this
#           b. Give the nft a placeholder name "Unknown Work" or creator's name
# 2. nft_collection list is empty

def extract_nft_names(nft_collection):
    # 1. Create a variable to store the result list
    result = []
    # 2. Iterate through the input list
    for nft in nft_collection:
        #   a. For each list item (dictionary), append the current dictionary["name"] value to result list
        if "name" in nft:
            result.append(nft["name"])
    # 3. Return result list
    return result


# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_4 = [
    {"creator": "SunsetArtist", "value": 8.9}
]

nft_collection_5 = []

nft_collection_6 = [
    {"creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))
print(extract_nft_names(nft_collection_4))
print(extract_nft_names(nft_collection_5))
print(extract_nft_names(nft_collection_6))
