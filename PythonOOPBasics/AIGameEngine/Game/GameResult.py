class GameResult:
    
    def __init__(self, over, winner):
        self.over = over
        self.winner = winner 

    def __str__(self) -> str:
        return "Game is Over : {}, Winner: {}".format(self.over, self.winner)
    

    def is_over(self):
        return self.over
    
    def get_winner(self):
        return self.winner