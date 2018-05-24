from CPU import CPU
from AssemblyManager import AssemblyManager




cpu=CPU() # main CPU object
assemblyManager=AssemblyManager() # main assembley manager object

cpu.memory.SetCellVal(0x001,"0x013") # setting cell 19 to 1

assembly=[
    "INP",
    "STA 19",
    "INP",
    "ADD 19",
    "OUT",
    "HLT"
          ] # assembly code for program

instructions=assemblyManager.ParseAssembly(assembly) # parsing assembly to hex with memory location
cpu.memory.LoadInstructions(instructions) # loading instructions into memory
cpu.Execute()

