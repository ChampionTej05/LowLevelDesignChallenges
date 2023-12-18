class Cell:
    def __init__(self, row, col):
        super().__init__()
        self.row = row
        self.col = col

    def __str__(self) -> str:
        return "Row : {} , col : {}".format(self.row, self.col)
    
    def get_row(self) -> int:
        return self.row 
    
    def get_col(self) -> int:
        return self.col