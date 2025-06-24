# Plan:
# 1. Create a dictionary to store frequencies of creators
#   a. Iterate through nft_collection, update the frequencies accordingly
# 2. Create a result list to store result
# 3. Iterate through frequency dictionary
#   a. If the current creator has a frequency greater than 1, append creator name to result list.
# 4. Return result list.

# Edge cases
# 1. Empty list
# 2. Creator key does not exist
#   a. Just don't add it to the frequency dictionary.
# 3. If data name is case sensitive?
#   a. Let's make creator names not case sensitive.


def identify_popular_creators(nft_collection):
    # 1. Create a dictionary to store frequencies of creators
    creator_frequencies = dict()
    #   a. Iterate through nft_collection, update the frequencies accordingly
    for nft in nft_collection:
        # edge case: creator key doesn't exist
        if not "creator" in nft:
            continue
        creator_frequencies[nft["creator"].lower()] = 1 if not nft["creator"].lower() in creator_frequencies else creator_frequencies[nft["creator"].lower()] + 1

    # 2. Create a result list to store result
    result = []

    # 3. Iterate through frequency dictionary
    for creator,frequency in creator_frequencies.items():
        #   a. If the current creator has a frequency greater than 1, append creator name to result list.
        if frequency > 1:
            result.append(creator)

    # 4. Return result list.
    return result


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_4 = []

nft_collection_5 = [
    {"name": "Crypto Kitty", "value": 10.5},
]

nft_collection_6 = [
    {"name": "Crypto Kitty", "creator": "cryptopets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "spaceart", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_7 = [
    {"name": "Crypto Kitty", "value": 10.5},
    {"name": "Crypto Kitties", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "spaceart", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
print(identify_popular_creators(nft_collection_4))
print(identify_popular_creators(nft_collection_5))
print(identify_popular_creators(nft_collection_6))
print(identify_popular_creators(nft_collection_7))