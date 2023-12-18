from Game.Board import Board
from Game.Cell import Cell

class TickTacToeBoard(Board):
    def __init__(self):
        super().__init__()
        #marking this as private
        self.__board = [["-" for j in range(0,3)] for i in range(0,3)]

    def get_cell(self, row, col):
        if 0 <= row < len(self.__board) and 0<= col < len(self.__board[0]):
            return self.__board[row][col] 
        
    def get_row(self, row):
        if 0<= row < len(self.__board):
            return self.__board[row]
        
    def show_board(self):
        print(self.__board)

    def set_cell(self, cell:Cell, symbol:str):
        if 0 <= cell.get_row() < len(self.__board) and 0<= cell.get_col() < len(self.__board[0]):
            self.__board [cell.get_row()][cell.get_col()] = symbol