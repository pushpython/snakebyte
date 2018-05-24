
class EnviromentalInterface:

    # programming enviroment
    def Interface(self):
        instructions=[]
        while True:
            console_input=input(">")
            if console_input == "c": EnviromentalInterface()
            elif console_input == "END": break
            else: instructions.append(console_input)
        return instructions

