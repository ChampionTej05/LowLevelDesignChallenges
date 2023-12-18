from Game.Cell import Cell
class Move:
    def __init__(self, cell: Cell):
        self.cell = cell

    def get_cell(self) -> Cell:
        return self.cell

    def __str__(self) -> str:
        return self.cell.__str__()