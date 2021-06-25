# import module
from geopy.geocoders import Nominatim
# initialize Nominatim API 
geolocator = Nominatim(user_agent="location finder")
place = "99501"
print("\nZipcode:",place)
location = geolocator.geocode(place)
print(location.address)