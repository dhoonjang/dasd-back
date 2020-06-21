class TravelGroup:
    def __init__(self, groupID, capacity, travelDate, travelDestination, memberList):
        self.groupID = groupID
        self.capacity = capacity
        self.memberList = memberList
        self.travelDate = travelDate
        self.travelDestination = travelDestination
        self.cr = ChatRoom()
        return
    def setTravelGroupInfo(self, traveldate, travelDestination, memberList):
        self.travelDate = travelDate
        self.travelDestination = travelDestination
        self.memberList = memberList
        return
    def getDestination(self):
        return self.travelDesination
    def getSchedule(self):
        return self.travelDate
    def getManWomanNum(self):
        return memberList.length
    def addMemberList(self, userID):
        self.memberList.push(userID)
        return
    def addChatMemberList(self, userID):
        return cr.addChatMemberList(userID)
    def requestRequestList(self):
        return DBHandler.instance().retrieveTravelGroup(self.groupID).requestList