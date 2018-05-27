from CPU import CPU
from AssemblyManager import AssemblyManager
from EnviromentalInterface import EnviromentalInterface

# Main CPU object
cpu=CPU()
# Main assembley manager object
assemblyManager=AssemblyManager()

# Main loops, isn't nessescary for running program
while True:
    # Getting array of assembly instructions from the console
    assembly=EnviromentalInterface.Interface()
    # Parsing assembly to hex with memory location
    instructions=assemblyManager.ParseAssembly(assembly)
    # If there is an error in the instructions, loop again
    if instructions == None: pass
    # If no errors...
    else:
        # Loading instructions into memory
        cpu.memory.LoadInstructions(instructions)
        # Execute the program
        cpu.Execute()

