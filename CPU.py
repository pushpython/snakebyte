from Memory import Memory

class CPU: # CPU class


    def __init__(self,):
        self.memory=Memory() # main memory object
        self.pc=0 # program counter
        self.accumulator=0 # accumulator

    def ex0x001(self,data): # HALT INSTRUCTION
        print("Halting Program")
        self.pc=-2 # the main loop will exit

    def ex0x002(self,loc): # ADD
        print("Adding location {}".format(loc))
        self.accumulator+=self.memory.GetCellVal(loc) # adding data to accumulator

    def ex0x003(self,loc): # SUBTRACT
        print("Subtracting location {}".format(loc))
        self.accumulator -= int(self.memory.GetCellVal(loc), 0)  # subtracting data to accumulator

    def ex0x004(self,loc): # STORE
        print("Storing at location {}".format(loc))
        self.memory.SetCellVal(self.accumulator,loc)

    def ex0x005(self,loc): # LOAD
        print("Loading location {}".format(loc))
        self.accumulator=self.memory.GetCellVal(loc)

    def ex0x006(self,data): # INPUT
        val=int(input("I/O {input}: "))
        self.accumulator=val

    def ex0x007(self,data): # OUTPUT
        print("OUT: "+str(self.accumulator))

    def ex0x008(self,loc): # BRANCH
        self.pc=int(loc,0)-1
        print("Branching to {}".format(self.pc))

    def ex0x009(self,loc): # BRANCH IF POSITIVE
        if self.accumulator % 2 == 0:
            self.pc=int(loc,0)-1
            print("Branching to {}".format(self.pc))
        else:
            pass

    def ex0x010(self,loc): # BRANCH IF ZERO
        if self.accumulator == 0:
            self.pc=int(loc,0)-1
            print("Branching to {}".format(self.pc))
        else:
            pass



    def Execute(self):

        hexToExecutor={"0x001":self.ex0x001, # corresponding opcode execution functions
                      "0x002":self.ex0x002,
                      "0x003":self.ex0x003,
                      "0x004":self.ex0x004,
                      "0x005":self.ex0x005,
                      "0x006":self.ex0x006,
                      "0x007":self.ex0x007,
                      "0x008": self.ex0x008,
                      "0x009": self.ex0x009,
                      "0x010": self.ex0x010,}
        # to execute do instructions.get("HLT")(params here)
        while self.pc > -1 and self.pc < len(self.memory.cells): # main exection loop

            instruction=self.memory.GetCellVal(hex(self.pc)) # getting the instruction at memory location self.pc
            opcode=instruction[0:5] # getting opcode
            data=instruction[5:9] # getting 4 bit data value


            try:
                hexToExecutor.get(opcode)(data) # executing instruction with data
            except:
                pass
            self.pc += 1  # incrementing program counter
