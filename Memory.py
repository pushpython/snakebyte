from Cell import Cell


class Memory():
    
    # Initialisation
    def __init__(self):
        # Initialises the memory cells
        self.cells = self.GenerateCells(64)

    # Initialises all memory cells with size 'size'
    def GenerateCells(self,size):
        
        # Creating array of cells, each cell provided an index i
        cells = [Cell(hex(i)) for i in range(size-1)]
        
        # Return the cells array
        return cells

    # Getting the value of a cell
    def GetCellVal(self,loc):
        # Converting the hex index to an integer
        index = int(loc, 0)
        # Returning the value of the cell with given index
        return self.cells[index].GetValue()

    # Function to set cell value with given value and location
    def SetCellVal(self, val, loc):
        # Converting the hex index to an integer
        index = int(loc,0)
        self.cells[index].SetValue(val)
        return True

    def LoadInstructions(self,instructions):
        for i in range(len(instructions)):
            self.SetCellVal(instructions[i][0],instructions[i][1])

        return True
