
'''
Our task is to create AI game engine that can solve any board game 

Let us start with basics skelete code of it 


'''
from API.GameEngine import GameEngine
from Game.Move import  Move
from Game.Cell import Cell
from Game.Player import Player

# constants 
TICK_TACK_TOE = "TickTackToe"

if __name__ == "__main__":

    # game_engine = GameEngine()
    # player1 = Player(symbol = "x")
    # tick_tak_toe_board = game_engine.start(game_type=TICK_TACK_TOE)
    # character  = "x"
    # move = Move(Cell(0,1))
    # print(move)
    # game_engine.move(tick_tak_toe_board, move, player1 )
    # print(tick_tak_toe_board)
    # game_result = game_engine.is_complete(tick_tak_toe_board)
    # print(game_result)
    # print(tick_tak_toe_board.show_board())


    game_engine = GameEngine()
    board = game_engine.start(game_type= TICK_TACK_TOE)
    #since X will be choosen by Opponent
    computer_player = Player(symbol = "O")

    #define opponent 

    opponent_player = Player(symbol="X")

    while (not game_engine.is_complete(board).is_over()):
        print("input row and col for play , your position is X")
        row = int(input("Row: "))
        col = int(input("Col : "))
        
        opponent_move = Move(Cell(row,col))
        game_engine.move(board, opponent_move, opponent_player )

        game_engine.show(board)

        game_result = game_engine.is_complete(board)
        print("Game Result : ", game_result)
        if(game_result.is_over()):
            print("game is over ")
            print("Winner: ", game_result.get_winner())
            break 

        computer_move = game_engine.suggest_move(board, computer_player) 
        print("Computer Played : ", computer_move)
        game_engine.move(board,computer_move, computer_player)

        print("board state ")
        game_engine.show(board)


    

