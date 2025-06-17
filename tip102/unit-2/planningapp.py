# We want to access a given artist's festival schedule.
# If schedule for artist not found, return a message with the value 'Artist not found'

# Edge cases
# 1. Account for capitalization?
# 2. Empty artist name

def get_artist_info(artist, festival_schedule):
    # 1. Get artist data in festival_schedule like festival_schedule[artist] or festival_schedule.get(artist)

    # Dictionary comprehension verison for replacing keys to lowercase
    # turn festival_schedule keys into lowercase
    # festival_schedule = {
    #     key.lower(): value for key, value in festival_schedule.items()        
    # }

    # Iteration version for replacing keys to lowercase
    festival_schedule_lowered = {}
    for key,value in festival_schedule.items():
        festival_schedule_lowered[key.lower()] = value

    festival_schedule = festival_schedule_lowered

    artist = artist.lower()

    # Single line version for getting artist data
    artist_data = None if not artist in festival_schedule else festival_schedule[artist] 

    # Multi-line version of getting artist data
    # if not artist in festival_schedule:
    #     artist_data = None
    # else:
    #     artist_data = festival_schedule[artist]


    # 2. If artist not found, return a message with artist not found
    if artist_data == None:
        return {'message' : 'Artist not found'}
    # 3. Otherwise, return data associated with artist
    else:
        return artist_data
    

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}



print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
print(get_artist_info("metallica", festival_schedule))