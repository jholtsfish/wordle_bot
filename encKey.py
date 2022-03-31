class key:
    def __init__(self):
        self.encNameKey = {}
        self.encPasswordKey = {}
    def AppendUserKey(self, userKey):
        self.encNameKey.update(userKey)
    def AppendPasswordKey(self, passwordKey):
        self.encPasswordKey.update(passwordKey)