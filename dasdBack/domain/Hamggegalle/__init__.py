class Hamggegalle:
    _instance = None
    def _getInstance(cls):
        return cls._instance
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance
    def __init__:
        return
    def createTravelGroup(self):
        return
    def enterInfo(self, travelDestination, travelDate, capacity):
        return
    def requestGroupList(self, travelDate, travelDestination):
        return DBHandler.instance().retrieveGroupList(travelDate, travelDestination)
    def applyToGroup(self, userID, groupID, tweet):
        return
    def requestRecommendation(self):
        return
    def requestTest(self):
        return
    def answerQuestions(self, answerSet):
        return
    def selectRegion(self, region):
        return
    def selectDestination(self, destination):
        return
    def requestGuesthouseList(self, destination):
        return DBHandler.instance().retrieveGuestHouseList(destination)
    def selectGuesthouse(self, postID):
        return
    def makeReservation(self, groupID, guestHouseID):
        return
    def endReservation(self):
        return
    def enterGuesthouseInfo(self, location, name, manCapacity, womavCapacity, price, auth):
        return
    def requestRequestList(self, groupID):
        return
    def approveMember(self, userID):
        return