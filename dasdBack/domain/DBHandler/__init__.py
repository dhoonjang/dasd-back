class DBHandler:
    _instance = None
    def _getInstance(cls):
        return cls._instance
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance
    def __init__:
        return
    def updateGroupInfo(self, travelDestination, travelDate, capacity, memberList, groupID):
        return
    def retrieveGroupList(self, travelDate, travelDestination):
        return
    def applyToGroup(self, userID, groupID, tweet):
        return
    def retrieveQuestionSet(self):
        return
    def retrieveTypeTable(self):
        return
    def retrieveRegionThemeList(self, tr):
        return
    def retrieveDestination(self, region, theme):
        return
    def retrieveGuestHouseList(self, destination):
        return
    def retrieveTravelGroup(self, groupID):
        return
    