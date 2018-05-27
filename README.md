# snakebyte
An open source basic CPU emulator with an assembly instruction set

This is by no means complex or advanced, it is simply a project that allows people to further understand process execution on a 'hardware level' (not exactly).

# Memory Location & literal value
To specify a literal number, such as ADD 1 *not* memory location 1, add a - prefix. ADD -1 will add 1 to the accumulator. ADD 1 will add the value at memory location 1 to the accumulator.

# Instruction Set
The system uses the same assembly instruction set as the Little Man Computer, which this project was inspired from

* **INP**           Inputting to the accumulator
* **OUT**           Outputting the value of the accumulator to the screen
* **ADD location**  Adding the value at the specified location to the accumulator
* **SUB location**  Subtracting the value at the specified location from the accumulator
* **STA location**  Storing the accumulator value at the specified location
* **LDA location**  Loading the accumulator with the value at the specified location 
* **BRA n**         Branch to instruction line n
* **BRP n**         Branch if the accumulator value is positive to instruction line n
* **BRZ n**         Branch if the accumulator is zero to the instruction line n
* **AND n**         Set accumulator to 1 if accumulator and specified data isn't 0
* **OR n**          Set accumulator to 1 if accumulator or specified data isn't 0
* **XOR n**         Set accumulator to 1 if accumulator or exclusively specified data isn't 0
