# Class defining a single memory location
class Cell():
    
    # Initialisation
    def __init__(self,loc):
        # Memory location index
        self.location=loc
        # Default value (in hex)
        self.value="0x000"
    
    # Function to set value
    def SetValue(self,val):
        self.value=val
        
    # Function to get value
    def GetValue(self):
        return self.value
