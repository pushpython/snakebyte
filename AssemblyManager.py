

class AssemblyManager:
    
    # Initialisation
    def __init__(self):
        # Dictionary containing keys for ASSEMBLY instructions & corresponding functions
        self.assembly_dictionary = \
                        {"HLT": self.hlt,
                         "ADD": self.add,
                         "SUB": self.sub,
                         "STA": self.sta,
                         "LDA": self.lda,
                         "INP": self.inp,
                         "OUT": self.out,
                         "BRA": self.bra,
                         "BRP": self.brp,
                         "BRZ": self.brz}
            
    # Function to parse assembly into hex opcodes with corresponding memory locations (returns tuple array)
    def ParseAssembly(self,assembly):
        # initialising the instructor function to None for error handling further down
        instruction=None
        # Irray containing the tuples
        intermediate=[]
        # Array containing syntax errors
        errors=[]
        # Looping through each Assembly instruction
        for i in range(len(assembly)):
            # Getting the instructioj opcode (Excluding additional data)
            instruction=assembly[i].split()[0]
            
           # NOT SURE IF THIS IS NEEDED self.assembly_dictionary.get(instruction)
            
            # Trying to get data from the instruction
            try:data=assembly[i].split()[1]
            # If there is no data, set data to None
            except:data=None
            
            # Try to return the hex tuple and append it to the intermediate array
            try:intermediate.append((self.assembly_dictionary.get(instruction)(hex(i),data))) # executing the relevant instruction and passing the memory location
            
            # If the instruction is incoreect or if there is an error, append errors with the error on line i
            except:errors.append("Incorect syntax on line {}".format(i))
            
        if len(errors) == 0:
            return intermediate
        else:
            print("Errors: {}".format(errors))
            return

    def hlt(self,location,val):
        address="0x001"
        if val==None:
            return (address, location)
        else:
            return (address+str(val),location)

    def add(self,location,val):
        address="0x002"
        if val==None:
            return (address, location)
        else:
            return (address+str(val),location)

    def sub(self,location,val):
        address="0x003"
        if val==None:
            return (address, location)
        else:
            return (address+str(val),location)

    def sta(self,location,val):
        address="0x004"
        if val==None:
            return (address, location)
        else:
            return (address+str(val),location)

    def lda(self,location,val):
        address="0x005"
        if val==None:
            return (address, location)
        else:
            return (address+str(val),location)

    def inp(self,location,val):
        address="0x006"
        if val==None:
            return (address, location)
        else:
            return (address+str(val),location)

    def out(self,location,val):
        address="0x007"
        if val==None:
            return (address, location)
        else:
            return (address+str(val),location)

    def bra(self,location,val):
        address="0x008"
        if val==None:
            return (address,location)
        else:
            return (address+str(val),location)

    def brp(self,location,val):
        address="0x009"
        if val==None:
            return (address,location)
        else:
            return (address+str(val),location)

    def brz(self,location,val):
        address="0x010"
        if val==None:
            return (address,location)
        else:
            return (address+str(val),location)
