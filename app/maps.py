from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent = 'MiniBus')

class Maps(object):

    def __init__(self):
        pass

    def get_coord_by_address(self, address):
        location = geolocator.geocode(address)
        print(location)
        print(location.latitude, location.longitude)

    def get_address_by_coord(self, width, longitude):
        coord = width + ", " + longitude
        location = geolocator.reverse(coord)
        print(location)

    #def get_stop_by_address(self):

    #def get_stop_by_coord(self):


if __name__ == '__main__':
    map = Maps()
    map.get_address_by_coord("45.0124143", "38.932524")
    map.get_coord_by_address("Бульвар Клары Лучко 12, Краснодар")