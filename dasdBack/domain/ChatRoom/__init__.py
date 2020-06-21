class ChatRoom:
    chagMemberList = []
    def __init__(self, groupID, userID):
        self.groupID = groupID
        self.chatMemberList.push(userID)
        return
    def addChatMemberList(self, userID):
        self.chatMemberList.push(userID)
        return