from Cell import Cell


class Memory():
    def __init__(self):
        self.cells = self.GenerateCells(64) # Initialises the memory

    def GenerateCells(self,size): # Initialises all memory cells

        cells = [Cell(hex(i)) for i in range(size-1)]

        # cells=[]
        # for i in range(size-1):
        #     cells.append(Cell(hex(i)))
        return cells

    def GetCellVal(self,loc): # getting the value of a cell
        index = int(loc, 0)
        return self.cells[index].GetValue()


    def SetCellVal(self, val, loc): # setting the value of a cell with location loc
        index = int(loc,0)
        self.cells[index].SetValue(val)
        return True

    def LoadInstructions(self,instructions):
        for i in range(len(instructions)):
            self.SetCellVal(instructions[i][0],instructions[i][1])

        return True
