

class AssemblyManager:
    def __init__(self):
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

    def ParseAssembly(self,assembly):
        instruction=None
        intermediate=[]
        errors=[]
        for i in range(len(assembly)):
            instruction=assembly[i].split()[0]
            self.assembly_dictionary.get(instruction)
            
            try:data=assembly[i].split()[1]
            except:data=None
            
            try:intermediate.append((self.assembly_dictionary.get(instruction)(hex(i),data))) # executing the relevant instruction and passing the memory location

            except:
                errors.append("Incorect syntax on line {}".format(i))
            
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
