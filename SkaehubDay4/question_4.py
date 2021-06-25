from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent = "countryfindr")
def get_country():
   location = geolocator.geocode("Mombasa")
   return location
print(get_country())