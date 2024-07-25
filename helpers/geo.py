

import math

def get_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
 
    # Calculate the differences between the latitude and longitude
    dlat = lat2 - lat1
    dlon = lon2 - lon1
 
    # Apply the haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
 
    # Calculate the distance in kilometers
    distance = 6371 * c
 
    # Return the distance in kilometers
    return distance 

