import geocoder
from geopy.geocoders import Nominatim
class location_extraction:
    def current_location():
        g = geocoder.ip('me')
        city=g.city
        country=g.country
        state=g.state
        return city,country
    # print(current_location())