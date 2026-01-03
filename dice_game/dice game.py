from random import randint as Generator

class PLAYER:

    def __init__(self,Name):
        self.Name = Name
        self.Score = 0
        self.Rolls_History = []
        self.Wins = 0

    def Reset(self):
        self.Score = 0
        self.Rolls_History = []

class ScoreBoard:

    def __init__(self,Players):
        """Score board class stores all data and players"""
        self.History = []
        self.Players = Players

    def Create_scoreboard(self):
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
        """Rolls the dice and has them stored in list"""
        Dice_Rolls = []
        input("Enter a character to roll the dices : ")
        print(f"You have rolled:",end = "")
        for _ in range(self.Dice_count):
            Curr_Roll = Generator(1,self.Dice_type)
            Dice_Rolls.append(Curr_Roll)
            print(f"| {Curr_Roll} |",end = "")
        print()
        return Dice_Rolls
    
    def Game_Loop(self):
        '''
        loop of the game
        '''
        current_Round = 1
        while True:
            print("-"*50)
            print(f"ROUND {current_Round}!")
            for id in self.Players:
                Player = self.Players[id]
                print(f"{Player.Name}'s Turn")
                Rolls = self.Roll_Dice(Player)
                Player.Rolls_History.append(Rolls)
                if self.Check_winner(Rolls):
                    return id
            print(f"END of ROUND {current_Round}")
            current_Round += 1
            
class Game_A(Game):

    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players,Goal_score,Reset_flag = 1,Reroll_flag = 0):
        super().__init__(Player_count,Dice_count,Dice_type,Game_type,Players)
        """Specilized game for a) Total score excedes a particular no"""
        self.Goal_score = Goal_score
        self.Reroll_flag = Reroll_flag
        self.Score_board = ScoreBoard(Players)
        self.Reset_number = Reset_flag

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
                if self.Reroll_flag:
                    if input("Want to rerolle (y/n) : ").lower() == "y":
                        Rolls = self.Roll_Dice(Player)
                Player.Rolls_History.append(Rolls)
                Player.Score  += sum(Rolls)
                if self.Reset_number in Rolls:
                    print(f"\U0001F605 Oops... you have rolled {self.Reset_number}\nScore reset!  \U0001F504")
                    Player.Score  =  0
                if Player.Score >= self.Goal_score:
                    return id
            print(f"END of ROUND {current_Round}")
            current_Round += 1
            self.Score_board.Create_scoreboard()
    
class Game_B(Game):

    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players, Goal_sequence):
        super().__init__(Player_count,Dice_count,Dice_type,Game_type,Players)

        """Specilized game for b) Who ever rolls  a particular sequence"""
        self.Goal_sequence = {}
        for number in set(Goal_sequence):
            self.Goal_sequence[number] = Goal_sequence.count(number)
        
    def Check_winner(self,Rolls):
        '''
        Checks win condition
        
        :param self: Description
        :param Rolls: Description
        '''
        for number in self.Goal_sequence.keys():
            if Rolls.count(number) < self.Goal_sequence[number]:
                return False
        return True     

class Game_C(Game):
    
    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players,Goal_sum):
        super().__init__(Player_count,Dice_count,Dice_type,Game_type,Players)

        """Specilized game for c) Get a particular sum in a role."""
        self.Goal_sum = Goal_sum

    def Check_winner(self,Rolls):
        if sum(Rolls) == self.Goal_sum:
            return True
        return False 

class Game_D(Game):

    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players,Rounds):
        super().__init__(Player_count,Dice_count,Dice_type,Game_type,Players)

        """Specilized game for d) Who could roll the max sum."""
        self.Rounds = Rounds

    def Game_Loop(self):
        current_Round = 1
        Max_id = 0
        Max_Score = 0
        while current_Round < self.Rounds + 1 :
            print("-"*50)
            print(f"ROUND {current_Round}!")
            for id in self.Players:
                Player = self.Players[id]
                print(f"{Player.Name}'s Turn")
                Rolls = self.Roll_Dice(Player)
                Player.Rolls_History.append(Rolls)
                if sum(Rolls) == self.Dice_count*self.Dice_type:
                    print("Wow! What a role. You got the max possible score ")
                    return id
                if Max_Score < sum(Rolls):
                    if  Max_id != id :
                        print(f"Oops {Player.Name} had beaten {self.Players[Max_id].Name} to claim first place. ")
                        Max_id = id
                    Max_Score = sum(Rolls)
                    
            print(f"END of ROUND {current_Round}")
            print(f"{self.Players[Max_id].Name} has the highest score with {Max_Score}")
            current_Round += 1
        return Max_id

def Game_intro():
    '''
    Gives intro about the game
    '''
    print(f"{'Dice Game'.center(50,'-')}")
    print("Welcome to Dice Game!")
    print("Rules of the Game:")
    print("Each players playes alternatively.")
    print("You could choose any type of the following Games.")
    print("(Based on the win conditions)")
    print("a) Total score excedes a particular no.\nb) Who ever rolls  a particular sequence.\nc) Get a particular sum in a role.\nd) Who could roll the max sum.""")
    print("-"*50)

def Game_start(no_of_players,Players,GAME):
    '''
    Selects the game type and replay condition
    '''
    Flag = "y"
    while Flag == 'y':
        id = GAME.Game_Loop()
        print("-"*50)
        print(f"Player {Players[id].Name} has won the Game. \U0001F3C6")
        print("Hears your Crown \U0001F451")
        Players[id].Wins += 1
        print("-"*50)
        for id in Players.keys():
            print(f"{Players[id].Name} no of Wins {Players[id].Wins}")
        print("-"*50)
        
        Flag = input("Want to play the same Game(y) : ").strip().lower()
        if Flag == 'y':
            if input("Want to have same Players? (y) : ").strip().lower() != 'y':
                no_of_players,Players = Game_Players()
                GAME.Players = Players
                GAME.Player_count  = no_of_players
                GAME.Score_board = ScoreBoard(Players)
            else:
                for player in Players.values():
                    player.Reset()
                    
    if input("Want to play a different Game? (y) : ").strip().lower() == "y":
        if input("Want to have same Players? (y) : ").strip().lower() != 'y':
            no_of_players,Players = Game_Players()
        else:
            for player in Players.values():
                player.Reset()
        GAME = Game_create(no_of_players,Players)
        Game_start(no_of_players,Players,GAME)
    else:
        print("-"*50)
        print("Thanks for Playing this Game.")
        print("Hope You Enjoyed it.")
        print("See you later. Bye!.")
        print("-"*50)
            
def Game_Players():
    """
    Creats the player base
    """
    no_of_players = input("Can you specify the no of players who are willing to play this game? : ").strip()
    while (not no_of_players.isnumeric() or (int(no_of_players) < 1 or int(no_of_players) > 10 )):
        print("Sorry the no of Players must be between 1-10.")
        no_of_players = input("Can you specify the no of players who are willing to play this game? : ").strip()
    no_of_players  = int(no_of_players)
    Players = {}
    for id in range(no_of_players):
        player = PLAYER(input(f"Enter player {id+1} name : ").strip().title())
        Players[id] = player
    return no_of_players,Players

def Game_create(no_of_players,Players):
    """
    basic game creation from user inputs(dices,sides,type of game)
    """
    print("Now lets create the game")

    DICES = input("Enter the no of dice : ").strip()
    while (not DICES.isnumeric() or (int(DICES) < 1 or int(DICES) > 10 ) ):
        print("Sorry the no of dice must be between 1-10")
        DICES = input("Enter the no of dice : ").strip()
    DICES = int(DICES)

    SIDES =input("Enter the no of sides of the dice: ").strip()
    while (not SIDES.isnumeric() or (int(SIDES) < 1 or int(SIDES) > 25 ) ):
        print("Sorry the no of sides must be between 1-24.")
        SIDES = input("Enter the no of sides of the dice: ").strip()
    SIDES = int(SIDES)

    TYPE = input("Enter the type of game (a or b or c or d): ").strip().lower()
    while TYPE not in "abcd":
        print("Invalid choice! Select a valid Type.")
        TYPE = input("Enter the type of game (a or b or c or d): ").strip().lower()

    if TYPE == "a":
        Reset_flag = input("Enter the numbere that when rolled would reset the score \n(enter n to not add this feature): ").strip().lower()
        Reroll_flag = input("Can there be a rerolle y/n: ").strip().lower()
        Goal_score = input("Enter the Score to reach : ").strip()
        while (not Goal_score.isnumeric() or int(Goal_score) < 1 ):
            print("sorry the Score should be a number greater than 0.")
            Goal_score = input("Enter the Score to reach : ").strip()
        if Reroll_flag == "y":
            Reroll_flag = 1
        if Reset_flag == "n":
            Reset_flag = '0'
        GAME = Game_A(no_of_players,DICES,SIDES,TYPE,Players,int(Goal_score),int(Reset_flag),Reroll_flag)
    elif TYPE == "b":
        Goal_sequence = list(map(int,input("Enter the sequence : ").split(" ")))
        while len(Goal_sequence) > DICES or set(Goal_sequence) - set(i for i in range(1,SIDES + 1 )) :
            print("Sorry the length of the sequence of dice is greater than no of dice or has invalid type")
            Goal_sequence = list(map(int,input("Enter the sequence : ").split(" "))) 
        GAME = Game_B(no_of_players,DICES,SIDES,TYPE,Players,Goal_sequence)
    elif TYPE == "c":
        Goal_sum = input("Enter the number to reach : ").strip()
        while (not Goal_sum.isnumeric() or int(Goal_sum) < 1 or int(Goal_sum) > DICES*SIDES or int(Goal_sum) < DICES):
            print(f"Sorry invalid choice Goal must be between {DICES} and {DICES*SIDES}")
            Goal_sum = input("Enter the number to reach : ").strip()
        GAME = Game_C(no_of_players,DICES,SIDES,TYPE,Players,int(Goal_sum))
    elif TYPE == "d":
        Rounds = input("Enter the number of rounds : ").strip()
        while (not Rounds.isnumeric() or int(Rounds) < 1 ):
            print(f"Sorry invalid choice Rounds must be greater Than 1")
            Rounds = input("Enter the number of rounds : ").strip()
        GAME = Game_D(no_of_players,DICES,SIDES,TYPE,Players,int(Rounds))

    return GAME

if __name__ == "__main__":
    Game_intro()
    no_of_players,Players = Game_Players()
    GAME = Game_create(no_of_players,Players)
    Game_start(no_of_players,Players,GAME)
