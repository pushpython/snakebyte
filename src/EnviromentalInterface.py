import os

class EnviromentalInterface:

    # programming enviroment
    @staticmethod
    def Interface():
        # File name for program
        program_name=input("filename: ")
        # Opening file
        with open(os.path.join(os.pardir, "res/"+program_name+".sbp"), "r") as file:
            # Getting array of instructions
            instructions = file.readlines()
        # Removing white space (e.g. /n etc)
        instructions = [i.strip() for i in instructions]
        print(instructions)
        return instructions
        
        
        
##    @staticmethod
##    def NewProgram():
##        instructions=[]
##        while True:
##            console_input=input(">")
##            if console_input == "c": EnviromentalInterface()
##            elif console_input == "END": break
##            else: instructions.append(console_input)
##        return instructions
##
##    @staticmethod
##    def LoadProgram(program_name):
##        with open(os.path.join(os.pardir, "res/"+program_name+".sbp"), "r") as file:
##            instructions = file.readlines()
##        instructions = [i.strip() for i in instructions]
##        print(instructions)
##        return instructions
        
