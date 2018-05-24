


# programming enviroment
def EnviromentInterface():
    instructions=[]
    while True:
        console_input=input(">")
        if console_input == "c": EnviromentalInterface()
        elif console_input == "END": break
        else: instructions.append(console_input)
    return instructions

instructions=EnviromentInterface()
print(instructions)
