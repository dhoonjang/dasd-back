class ApplicationRequest:
    def __init__(self, userID, groupID, tweet):
        self.userID = userID
        self.groupID = groupID
        self.tweet = tweet
        DBHandler.instance().applyToGroup(userID, groupID, tweet)
        return