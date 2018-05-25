from CPU import CPU
from AssemblyManager import AssemblyManager
from EnviromentalInterface import EnviromentalInterface




cpu=CPU() # main CPU object
assemblyManager=AssemblyManager() # main assembley manager object

while True:
    assembly=EnviromentalInterface.Interface()
    instructions=assemblyManager.ParseAssembly(assembly) # parsing assembly to hex with memory location
    if instructions == None: print("Restarting")
    else:
        cpu.memory.LoadInstructions(instructions) # loading instructions into memory
        cpu.Execute()

