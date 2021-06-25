from geopy.geocoders import Nominatim
# initialize Nominatim API 
geolocator = Nominatim(user_agent="locationfinder")
def city_state_country(accept_corrdinate):
    # to capture Latitude & Longitude
    location = geolocator.reverse(accept_corrdinate, exactly_one=True)
    address = location.raw['address']
    # traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    return city, state, country,code,zipcode
    # Latitude & Longitude input
print(city_state_country("1.2921, 36.8219"))

