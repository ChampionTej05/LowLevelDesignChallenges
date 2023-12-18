from Game import Board
from Game.Move import  Move
from Game.GameResult import GameResult
from Boards.TickTacToeBoard import TickTacToeBoard
from Game.Player import Player
from Game.Cell import Cell

class GameEngine:
    
    def start(self, game_type:str) -> Board:
        if game_type == "TickTackToe":
            return TickTacToeBoard()
        
        raise Exception("Invalid Game Argument ")
    
    def move(self,board: Board, move: Move, player:Player):

        #set the character on the board to move 
        board.set_cell(move.get_cell(), player.symbol)
        
    
    def show(self,board:Board) -> None:
        if not isinstance(board, TickTacToeBoard):
            raise Exception("Not possible at this point of time ")

        print(board.show_board())

    def suggest_move(self, board:Board, player: Player) -> Move:

        if not isinstance(board, TickTacToeBoard):
            raise Exception("Not possible at this point of time ")

        for i in range(0,3):
            for j in range(0,3):
                if board.get_cell(i, j) == "-":
                    return Move(Cell(i, j))
        
        raise Exception("No move is possible from computer, Game seems to be done")

    def is_complete(self, board: Board) -> GameResult:
        '''
        check if the game is complete or not 
        this should return GameResult Object
        '''

        if not isinstance(board, TickTacToeBoard):
            print("Not Implemented yer")
            return
        
        firstCharacter = None 
        
        for i in range(0,3):
            firstCharacter = board.get_cell(i,0)
            if firstCharacter != "-":
                row = board.get_row(i)
                if row.count(firstCharacter) == 3:
                    return GameResult(over=True, winner=firstCharacter)
        
        #check for col 
        for j in range(0,3):
            firstCharacter = board.get_cell(0,j)
            if firstCharacter != "-":
                count = 0
                for i in range(0,3):
                    if board.get_cell(i,j) == firstCharacter:
                        count+=1
                if firstCharacter != "-"  and count == 3:
                    return GameResult(over=True, winner=firstCharacter)
                
        #check for diagonal (i=j)
        firstCharacter = board.get_cell(0,0)
        over = True
        if firstCharacter != "-":
            for i in range(1,3):
                if board.get_cell(i,i) != firstCharacter:
                    over = False 
            if over:
                return GameResult(over = True, winner= firstCharacter)
        
    
        #check for reverse diagonal (i = 2-j)

        firstCharacter = board.get_cell(0,2)
        over = True 
        if firstCharacter != "-":
            for i in range(0,3):
                if board.get_cell(i,2-i) != firstCharacter:
                    over = False 
            if over:
                return GameResult(over = True, winner= firstCharacter)
        
        # check if complete board is filled 
        for i in range(0,3):
            rowCount = board.get_row(i).count("-")
            # print("RowCount ", rowCount)
            if rowCount !=0:
                return GameResult(over = False, winner = "-")
            
        return GameResult(over = True, winner = "-")