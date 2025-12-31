from random import randint as Generator
class PLAYER:

    def __init__(self,Name):
        self.Name = Name
        self.Score = 0
        self.Rolles_History = []

class ScoreBoard:

    def __init__(self,Players):
        """Score board class stores all data and players"""
        self.History = []
        self.Players = Players

    def Creat_scoreboard(self):
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

        for id in self.Players.keys():
            Player = self.Players[id]
            Player_col_length = max(Player_col_length,Player.Score)
            Score_col_length = max(Score_col_length,Player.Score)

        Score_Table.append((Player_col_length + Score_col_length + Gap) * "-")
        Score_Table.append(f"| {'SCOREBOARD':^{Player_col_length + Score_col_length + Gap//2}} |")
        Score_Table.append((Player_col_length + Score_col_length + Gap) * "-")
        Score_Table.append(f"| {'players':^{Player_col_length}} | {'Scores':^{Score_col_length}} |")
        Score_Table.append((Player_col_length + Score_col_length + Gap) * "-")

        for id in self.Players.keys():
            Player = self.Players[id]
            Score_Table.append(f"| {Player.Name:^{Player_col_length}} | {str(Player.Score):^{Score_col_length }} |")
        Score_Table.append((Player_col_length + Score_col_length + Gap) * "-")

        self.Cur_Table = Score_Table
        self.Player_col_length = Player_col_length
        self.Score_col_length = Score_col_length
        self.History.append(self.Cur_Table)
        self.Display_Score()

    def Display_Score(self):
        for row in self.Cur_Table:
            print(row)

class Game:

    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players):
        """Creates a game by using user inputs"""
        self.Player_count = Player_count
        self.Dice_count = Dice_count
        self.Dice_type = Dice_type
        self.Game_type = Game_type
        self.Players = Players

    def Roll_Dice(self,Player):
        """Rolles the dice and has them stored in list"""
        Dice_Rolls = []
        input("Enter a character to roll the dices : ")
        print(f"You have rolled:",end = "")
        for _ in range(self.Dice_count):
            Curr_Roll = Generator(1,self.Dice_count)
            Dice_Rolls.append(Curr_Roll)
            print(f"| {Curr_Roll} |",end = "")
        print()
        return Dice_Rolls
            
class Game_A(Game):

    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players):
        super().__init__(Player_count,Dice_count,Dice_type,Game_type,Players)
        """Specilized game for a) Total score excedes a particular no"""

        temp1 = input("Enter the numbere that when rolled would reset the score \n(enter n to not add this feature): ").lower()
        temp2 = input("Can there be a rerolle y/n: ").lower()
        self.Value = int(input("Enter the Score to reach : "))
        self.Reroles = 0
        self.Score_board = ScoreBoard(Players)
        if temp1 == "n":
            temp1 = 0
        self.Reset_number = int(temp1)
        if temp2 == "y":
            self.Reroles = 1

    def Game_Loop(self):
        current_Round = 1
        print("Lets Start the Game")
        while True:
            print("-"*50)
            print(f"ROUND {current_Round}!")
            for id in self.Players:
                Player = self.Players[id]
                print(f"{Player.Name}'s Turn :")
                Rolls = self.Roll_Dice(Player)
                if self.Reroles:
                    if input("Whant to rerolle (y/n) : ").lower() == "y":
                        Rolls = self.Roll_Dice(Player)
                Player.Rolles_History.append(Rolls)
                Player.Score  += sum(Rolls)
                if self.Reset_number in Rolls:
                    print(f"\U0001F605 Oops... you have rolled {self.Reset_number}\nScore reset!  \U0001F504")
                    Player.Score  =  0
                if Player.Score >= self.Value:
                    return id
            print(f"END of ROUND {current_Round}")
            current_Round += 1
            self.Score_board.Creat_scoreboard()

class Game_B(Game):
    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players):
        super.__init__(Player_count,Dice_count,Dice_type,Game_type,Players)
        """Specilized game for b) Who ever rolls  a particular sequence"""
        self.Goal_sequence = list(map(int,input("Enter the sequence").split(" ")))
        while len(self.Goal_sequence) < self.Dise_count:
            print("Sorry the length of the sequence of dice is greater than no of dice")
            sequence = list(map(int,input("Enter the sequence").split(" ")))
            self.Goal_sequence = {}
            for number in set(sequence):
                self.Goal_sequence[number] = sequence.count(number)
            
    def Check_winner(self,Rolls):
        for number in self.Goal_sequence.keys():
            if Rolls.count(number) != self.Goal_sequence[number]:
                return False
        return True     

    def Game_Loop(self):
        current_Round = 1
        while True:
            print(f"ROUND {current_Round}!")
            for id in self.Players:
                Player = self.Players[id]
                print(f"{Player}'s Turn")
                Rolls = self.Roll_Dice(Player)
                Player.Rolles_History.append(Rolls)
                if self.Check_winner(Rolls):
                    return id
            print(f"END of ROUND {current_Round}")
            current_Round += 1

class Game_C:
    pass

class Game_D:
    pass

def Game_intro():
    print(f"{'Dice Game'.center(50,'-')}")
    print("Welcome to Dice Game!")
    print("Rules of the Game:")
    print("Each players playes alternatively.")
    print("You could choose any type of the following Games.")
    print("(Based on the win conditions)")
    print("a) Total score excedes a particular no.\nb) Who ever rolls  a particular sequence.\nc) Get a particular sum in a role.\nd) Who could roll the max sum.""")
    print("-"*50)

def Game_initial():
    print("Now lets create the game")
    Players = {}
    DICES = int(input("Enter the no of dice : "))
    SIDES = int(input("Enter the no of sides of the dice: "))
    no_of_players = int(input("Can you specify the no of players who are willing to play this game? : "))
    for id in range(no_of_players):
        player = PLAYER(input(f"Enter player {id+1} name : ").title())
        Players[id] = player
    while True:
        TYPE = input("Enter the type of game (a or b or c or d): ").lower()
        if TYPE not in "abc":
            print("Invalid choice! Try again")
            continue
        break
    if TYPE == "a":
        GAME = Game_A(no_of_players,DICES,SIDES,TYPE,Players)
    elif TYPE == "b":
        GAME = Game_B(no_of_players,DICES,SIDES,TYPE,Players)
    elif TYPE == "c":
        GAME = Game_C(no_of_players,DICES,SIDES,TYPE,Players)
    elif TYPE == "d":
        GAME = Game_D(no_of_players,DICES,SIDES,TYPE,Players)
    GAME.Game_Loop()
    print(f"Player {Players[id].Name} has won the Game. \U0001F3C6")
    print("Hears your Crown \U0001F451")
    if TYPE == "a":
        print("Final Score Board.")

if __name__ == "__main__":
    Game_intro()
    Game_initial()



    
    


        
    















