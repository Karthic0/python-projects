from random import randint as Generator
class Palyers:

    def __init__(self,Name):
        self.Name = Name
        self.Score = 0
        self.Previous_rolles = []

class ScoreBoard:

    def __init__(self,Players):
        '''
        Creates the scoreboard 
        ------------------
        |   scoreboard   |
        ------------------
        | player | score |
        
        '''
        Player_col_length = 7
        Score_col_length = 6
        Gap = 7
        Score_Table = []

        for Player in range(Players):
            Player_col_length = max(Player_col_length,Player.Score)
            Score_col_length = max(Score_col_length,Player.Score)

        Score_Table.append((Player_col_length + Score_col_length + Gap) * "-")
        Score_Table.append(f"| {'SCOREBOARD':^{Player_col_length + Score_col_length + Gap//2}} |")
        Score_Table.append((Player_col_length + Score_col_length + Gap) * "-")
        Score_Table.append(f"| {'players':^{Player_col_length}} | {'Scores':^{Score_col_length}} |")
        Score_Table.append((Player_col_length + Score_col_length + Gap) * "-")

        for Player in range(Players):
            Score_Table.append(f"| {Player:^{Player_col_length}} | {str(Players[Player]['Score']):^{Score_col_length }} |")
        Score_Table.append((Player_col_length + Score_col_length + Gap) * "-")

        self.Score_Table = Score_Table
        self.Player_col_length = Player_col_length
        self.Score_col_length = Score_col_length

    def Display_Score(self):
        for row in self.Score_Table:
            print(row)

    
class Game:

    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Reset_condition):
        self.Player_count = Player_count
        self.Dise_count = Dice_count
        self.Dice_type = Dice_type
        self.Game_type = Game_type
        self.Reset_condition = Reset_condition


    
    def Roll_Dice(self,Player):
        Dice_Rolls = []
        print(f"You have rolled")
        for _ in range(self.Dice_type):
            curr_roll = Generator(1,self.Dise_count)
            Dice_Rolls.append(curr_roll)
            print(f"| {curr_roll} |",end = "")
            if curr_roll == self.Reset_condition:
                print(f"\n Ops u have rolled {curr_roll} its Reset time")
                
            



    
    


        
    








































"""
    

def Game(Players,VALUES,SIDES,DICES):

    current_Round = 1
    while True:
        print(f"ROUND {current_Round}!")
        for player in Players:
            print(f"{player}'s Turn")
            print(f"{player} Rolled")
            Players[player]['Score'] += Roll_Dice(DICES,SIDES)
            if Players[player]['Score'] > VALUES:
                return player
        print(f"END of ROUND {current_Round}")
        current_Round += 1
        Display_Score(Players,VALUE)



# intro and rules
print(f"{'Dice Game'.center(50,'-')}")
print("Welcome to Dice game!")
print("Rules of the game:")
print("Each players playes alternatively")
print("Who ever's sum exeedes a specific range wins!")
print("-"*50)

#game setup
print("lets start the game!")
Players = {}
no_of_players = int(input("Can you specify the no of players who are willing to play this game? : "))
for i in range(no_of_players):
    Players[input(f"Enter player {i} name : ")] = {"Score" : 0}
VALUE = int(input("Enter the win score of the game: "))
DICES = int(input("Enter the no of dice to be rolled: "))
SIDES = int(input("Enter the no of sides of the dice: "))

winner = Game(Players,VALUE,SIDES,DICES)
print(f"Player {winner} has won the game")
"""