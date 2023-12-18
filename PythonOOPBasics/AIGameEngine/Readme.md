

# Game AI Enginer 


## Refactor 1
- Organise the code classes into individual classes under packages
- Packages could be 
  - Game (Things associated with Game)
    - Board 
    - Move 
    - GameResult 
    - Player ( we can keep this separate too as User)
  - API (this is where interaction with user will happen )
    - GameEngine 
  - Boards (to store type of board coming in future, we can also put this under Game)
    - TickTacToeBoard


## Refactor 2:
- Where should getCell and setCell be defined ? 
  - Mostly all boards will have cells but currently we are not sure, for what type of boards, we are writing 
  - so let us keep the cells in tick tac toe board class (instead of parent class)
- How to define Move 
  - Move consists of CELL which identifies each part of Board 
  - Let us define Cell class consisting of Row and Col 
  - In Move class, Cell is returned