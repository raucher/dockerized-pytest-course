class Point:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def get_lat_long(self):
        return (self.lat, self.lon)
