class Cell():
    def __init__(self,loc):
        self.location=loc
        self.value="0x000"

    def SetValue(self,val):
        self.value=val

    def GetValue(self):
        return self.value
