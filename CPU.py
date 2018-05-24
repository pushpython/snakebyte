from Memory import Memory

class CPU: # CPU class


    # initialisation
    def __init__(self):
        # main memory object
        self.memory=Memory()
        # program counter
        self.pc=0
        # accumulator
        self.accumulator=0

    def ex0x001(self,data): # HALT INSTRUCTION
        print("Halting Program")
        # the main loop will exit
        self.pc=-2

    def ex0x002(self,loc): # ADD
        print("Adding location {}".format(loc))
        # adding data at specified memory location to accumulator
        self.accumulator+=self.memory.GetCellVal(loc)

    def ex0x003(self,loc): # SUBTRACT
        print("Subtracting location {}".format(loc))
        # subtracting data at specified location to accumulator
        self.accumulator -= int(self.memory.GetCellVal(loc), 0)

    def ex0x004(self,loc): # STORE
        print("Storing at location {}".format(loc))
        # storing accumulator value at specified memory location
        self.memory.SetCellVal(self.accumulator,loc)

    def ex0x005(self,loc): # LOAD
        print("Loading location {}".format(loc))
        # loading value at specified memory location to accumulator
        self.accumulator=self.memory.GetCellVal(loc)

    def ex0x006(self,data): # INPUT
        # setting accumulator value to user input
        self.accumulator=int(input("I/O {input}: "))

    def ex0x007(self,data): # OUTPUT
        # outputting accumulator value to the console
        print("OUT: "+str(self.accumulator))

    def ex0x008(self,loc): # BRANCH
        print("Branching to {}".format(loc))
        # setting the program counter to the specified location
        # NOTE -1 required as the pc counter is incremented at the end of the loop and so is updated before the next instruction can run
        self.pc=int(loc,0)-1
        

    def ex0x009(self,loc): # BRANCH IF POSITIVE
        #checking if the accumulator is positive
        if self.accumulator % 2 == 0:
            # if so, set the pc value to the specified value
            self.pc=int(loc,0)-1
            print("Branching to {}".format(self.pc))
        else:
            # if not, pass
            pass

    def ex0x010(self,loc): # BRANCH IF ZERO
        # checking if the accumulator is 0
        if self.accumulator == 0:
            # if so, set the pc value to the specified value
            self.pc=int(loc,0)-1
            print("Branching to {}".format(self.pc))
        else:
            # if not, pass
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
