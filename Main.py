from CPU import CPU
from AssemblyManager import AssemblyManager
from EnviromentalInterface import EnviromentalInterface




cpu=CPU() # main CPU object
assemblyManager=AssemblyManager() # main assembley manager object

cpu.memory.SetCellVal(0x001,"0x013") # setting cell 19 to 1

assembly=EnviromentalInterface.Interface()

instructions=assemblyManager.ParseAssembly(assembly) # parsing assembly to hex with memory location
cpu.memory.LoadInstructions(instructions) # loading instructions into memory
cpu.Execute()

