class Test:
    def __init__(self):
        self.questionSet = None
        self.typeTable = None
        return
    def getTest(self):
        self.questionSet = DBHandler.instance().retrieveQuestionSet()
        self.typeTable = DBHandler.instance().retrieveTypeTable()
        return questionSet, typeTable
    def getTestResult(self, answerSet):
        return calcTestResult(answerSet, questionSet, typeTable)