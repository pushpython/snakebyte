from Memory import Memory

# CPU class
class CPU:


    # Initialisation
    def __init__(self):
        # main memory object
        self.memory=Memory()
        # program counter
        self.pc=0
        # accumulator
        self.accumulator=0

    # HALT INSTRUCTION
    def ex0x001(self,data):
        print("Halting Program")
        # the main loop will exit
        self.pc=-2

    # ADD
    def ex0x002(self,loc):
        print("Adding location {}".format(loc))
        # adding data at specified memory location to accumulator
        self.accumulator+=self.memory.GetCellVal(loc)

    # SUBTRACT
    def ex0x003(self,loc):
        print("Subtracting location {}".format(loc))
        # subtracting data at specified location to accumulator
        self.accumulator -= int(self.memory.GetCellVal(loc), 0)

    # STORE
    def ex0x004(self,loc):
        print("Storing at location {}".format(loc))
        # storing accumulator value at specified memory location
        self.memory.SetCellVal(self.accumulator,loc)

    # LOAD
    def ex0x005(self,loc):
        print("Loading location {}".format(loc))
        # loading value at specified memory location to accumulator
        self.accumulator=self.memory.GetCellVal(loc)

    # INPUT
    def ex0x006(self,data):
        # setting accumulator value to user input
        self.accumulator=int(input("I/O {input}: "))

    # OUTPUT
    def ex0x007(self,data):
        # outputting accumulator value to the console
        print("OUT: "+str(self.accumulator))

    # BRANCH
    def ex0x008(self,loc):
        print("Branching to {}".format(loc))
        # setting the program counter to the specified location
        # NOTE -1 required as the pc counter is incremented at the end of the loop and so is updated before the next instruction can run
        self.pc=int(loc,0)-1
        

    # BRANCH IF POSITIVE
    def ex0x009(self,loc):
        #checking if the accumulator is positive
        if self.accumulator % 2 == 0:
            # if so, set the pc value to the specified value
            self.pc=int(loc,0)-1
            print("Branching to {}".format(self.pc))
        else:
            # if not, pass
            pass

    # BRANCH IF ZERO
    def ex0x010(self,loc):
        # checking if the accumulator is 0
        if self.accumulator == 0:
            # if so, set the pc value to the specified value
            self.pc=int(loc,0)-1
            print("Branching to {}".format(self.pc))
        else:
            # if not, pass
            pass

    # AND
    def ex0x011(self,loc):
        # checking if the accumulator is 0 (False) and the memory location value is 0 (False)
        if bool(self.accumulator) != False and bool(self.memory.GetCellVal(loc)) != False:
            self.accumulator = 1
        else:
            self.accumulator = 0

    # OR
    def ex0x012(self,loc):
        # checking if the accumulator is 0 (False) or the memory location value is 0 (False)
        if bool(self.accumulator) != False or bool(self.memory.GetCellVal(loc)) != False:
            self.accumulator = 1
        else:
            self.accumulator = 0

    # XOR
    def ex0x013(self,loc):
        # checking if the accumulator is 0 or the memory location value is 0 exclusively
        if bool(self.accumulator) != bool(self.memory.GetCellVal(loc)):
            self.accumulator = 1
        else:
            self.accumulator = 0


    # Function to execute the program
    def Execute(self):
        
        # Corresponding opcode execution functions (Note this excludes additional data)   
        hexToExecutor={"0x001":self.ex0x001, "0x002":self.ex0x002, "0x003":self.ex0x003, "0x004":self.ex0x004, "0x005":self.ex0x005,
                       "0x006":self.ex0x006,"0x007":self.ex0x007,"0x008": self.ex0x008,"0x009": self.ex0x009,"0x010": self.ex0x010,
                       "0x011":self.ex0x011,"0x012":self.ex0x012,"0x013":self.ex0x013}
        
        # Main loop to execute each instruction
        while self.pc > -1 and self.pc < len(self.memory.cells):

            # Getting the instruction at memory location of the program counter
            instruction=self.memory.GetCellVal(hex(self.pc))
            # Getting the opcode for that instruction
            opcode=instruction[0:5]
            # Getting 4 bit data value (If specified)
            data=instruction[5:9]

            # Trying to execute operation with data
            try:hexToExecutor.get(opcode)(data)
            # If errors returned, pass
            except:
                print("UGHHH {}".format(opcode))
                pass
            
            # Incrementing program counter
            self.pc += 1 
