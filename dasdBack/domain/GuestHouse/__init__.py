class GuestHouse:
    def __init__(self, guestHouseID):
        self.guestHouseID = guestHouseID
        self.location = None
        self.name = None
        self.manCapacity = None
        self.womanCapacity = None
        self.price = None
        self.auth = None
        return
    def registerInfo(self, location, name, manCapacity, womanCapacity, price, auth):
        self.location = location
        self.name = name
        self.manCapacity = manCapacity
        self.womanCapacity = womanCapacity
        self.price = price
        self.auth = auth
        return
    def getGuestHouseInfo(self):
        return