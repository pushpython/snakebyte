from CPU import CPU
from AssemblyManager import AssemblyManager
from EnviromentalInterface import EnviromentalInterface




cpu=CPU() # main CPU object
assemblyManager=AssemblyManager() # main assembley manager object

while True: # Main loops, isn't nessescary for running program
    assembly=EnviromentalInterface.Interface() # Getting array of assembly instructions from the console
    instructions=assemblyManager.ParseAssembly(assembly) # Parsing assembly to hex with memory location
    if instructions == None: print("Restarting") # If there is an error in the instructions, loop again
    else: # If no errors...
        cpu.memory.LoadInstructions(instructions) # Loading instructions into memory
        cpu.Execute() # Executing program

