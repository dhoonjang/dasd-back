class DestinationRecommendation:
    def __init__(self, userID):
        self.userID = userID
        self.region = None
        self.destination = None
        self.test = None
        self.testResult = None
        return
    def createTest(self):
        return Test().getTest()
    def requestRegionThemeList(self, answerSet):
        self.testResult = test.getTestResult(answerSet)
        return DBHandler.instance().retrieveRegionThemeList(self.testResult)
    def setRegion(self, region):
        self.region = region
        return
    def setDestination(self, destination):
        self.destination = destination
        return
    def getDestination(self):
        return self.destination