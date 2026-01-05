"""
Dice Game Project
Author: Karthic
Description: A multi-mode dice game using OOP.
"""

from random import randint as Generator

class PLAYER:
    """
    Represents a player in the game.

    Attributes:
        Name (str): Name of the player.
        Score (int):Total score of the player(Game_a).
        Rolls_History: Histroy of Rolls by the player.
        Wins (int): Total number of games player has won.
    """

    def __init__(self,Name):
        """
        Initializes a new player.

        Args:
            Name (str): Name of the player.
        """
        self.Name = Name
        self.Score = 0
        self.Rolls_History = []
        self.Wins = 0

    def Reset(self):
        """
        Resets the Score and Rolls_History of the player.
        Called when playing another game.
        """
        self.Score = 0
        self.Rolls_History = []

class ScoreBoard:
    """
    Represents the scoreboard.
    (stores data about scores of each round).
    """

    def __init__(self,Players):
        """
        Initializes the scoreboard.
        
        Attribute:
            History (list(int)): Has data about scores on each round.
            Players (dictionary): Has the objects of players along with their IDs.
        """
        self.History = []
        self.Players = Players

    def create_scoreboard(self):
        """
        Creates the scoreboard in the formate of
        ------------------
        |   scoreboard   |
        ------------------
        | player | score |
        
        """
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
        self.display_Score()

    def display_Score(self):
        """
        Displays the created scoreboard for each round.
        """
        for row in self.Cur_Table:
            print(row)

class Game:
    """
    Represents the game played.

    Attributes:
        Player_count (int): Number of players.
        Dice_count (int): Number of Dice.
        Dice_type (int): Number of sides of the dice.
        Game_type (str): Type of game (a or b or c or d).
        Players (dictionary): Has the objects of players along with their IDs.
        Reroll_flag (bool): Is there reroll or not.

    """
    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players):
        """
        Initializes the game 
        
        Args:
            Player_count (int): Number of players.
            Dice_count (int): Number of Dice.
            Dice_type (int):  Number of sides of the dice.
            Game_type (str): Type of game (a or b or c or d).
            Players (dictionary): Has the objects of players along with their IDs.
        """
        self.Player_count = Player_count
        self.Dice_count = Dice_count
        self.Dice_type = Dice_type
        self.Game_type = Game_type
        self.Players = Players
        self.Reroll_flag = False

    def display_rolls(self,Dice_Rolls):
        """
        Displays the current rolls.
        
        Args:
            Dice_Rolls (list(int)): list of values that has current rolls.
        """
        print(f"You have rolled:| {' | '.join(list(map(str,Dice_Rolls)))} |")
        
    def roll_dice(self,Player):
        """
        Rolls the dices according to number of dice and type.
        (rolls two times if there is reroll)

        Args:
            Player: Player object for the current player.

        returns : 
            List(int): final list of dice roll values.
        """
        Dice_Rolls_1 = []
        Dice_Rolls_2 = []
        input("Enter a character to roll the dices : ")
        print(f"You have rolled:",end = "")
        for _ in range(self.Dice_count):
            Curr_Roll_1= Generator(1,self.Dice_type)
            Curr_Roll_2= Generator(1,self.Dice_type)
            Dice_Rolls_1.append(Curr_Roll_1)
            Dice_Rolls_2.append(Curr_Roll_2)
        self.display_rolls(Dice_Rolls_1)
        Dice_Rolls = Dice_Rolls_1

        if self.Reroll_flag and input("Want to reroll (y/n) : ").lower() == "y":
            self.display_rolls(Dice_Rolls_2)
            Dice_Rolls = Dice_Rolls_2

        Player.Rolls_History.append(Dice_Rolls)
        Player.Score  += sum(Dice_Rolls)

        return Dice_Rolls
    
    def game_loop(self):
        """
        Main loop of the game.

        Returns:
            int : ID of the winner.
        """
        current_Round = 1
        while True:
            print("-"*50)
            print(f"ROUND {current_Round}!")
            for id in self.Players:
                Player = self.Players[id]
                print(f"{Player.Name}'s Turn")
                Rolls = self.roll_dice(Player)
                if self.Check_winner(Rolls,Player):
                    return id
            print(f"END of ROUND {current_Round}")
            current_Round += 1
            if self.Game_type == 'a' :
                self.Score_board.create_scoreboard()
            
class Game_A(Game):
    """
    Represents Game A where you should exceed a targetsum to win.
    (child of Game)(inherits from game)

    Attributes:
        (all Attributes from Game)
        Goal_score (int) : Target value.
        Score_board (ScoreBoard): Scoreboard object for tracking scores.
        Reset_number (int): Number when rolled would reset the score of player.

    """

    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players,Goal_score,Reset_flag = 1,Reroll_flag = False):
        """ 
        Initializes of Game A.(Inherits from game.)

        Args:
            Reset_flag (int): Number which rolled would reset the score    
        """
        super().__init__(Player_count,Dice_count,Dice_type,Game_type,Players)

        self.Goal_score = Goal_score
        self.Reroll_flag = Reroll_flag
        self.Score_board = ScoreBoard(Players)
        self.Reset_number = Reset_flag

    def Check_winner(self,Rolls,Player):
        """ 
        Checks the win condition of the game and resets the score if reset number is rolled.

        Args:
            Rolls (list(int)) : List of current rolls
            Player (PLAYER ) : Current player object of PLAYER 
        Returns:
            Bool: if current player is the winner returns true 
        """
        if self.Reset_number in Rolls:
            print(f"\U0001F605 Oops... you have rolled {self.Reset_number}\nScore reset!  \U0001F504")
            Player.Score  =  0
        if Player.Score >= self.Goal_score:
            return True
        return False
    
class Game_B(Game):
    """
    Represents Game B where you have to roll a sequence inorder to win.
    (child of Game)(inherits from game)

    Attributes:
        (all Attributes from Game)
        Goal_sequence (dictionary): Number from goal sequence as key and count of it as values. 
    """

    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players, Goal_sequence):
        """ 
        Initializes of Game B.(Inherits from game.)

        Args:
            Goal_sequence (list(int)): Goal sequence to be rolled.    
        """
        super().__init__(Player_count,Dice_count,Dice_type,Game_type,Players)

        self.Goal_sequence = {}
        for number in set(Goal_sequence):
            self.Goal_sequence[number] = Goal_sequence.count(number)
        
    def Check_winner(self,Rolls,Player):
        """
        Checks whether the current rolls contain win sequence.
        
        Args:
            Rolls (list(int)) : List of current rolls.
            Player (PLAYER ) : Current player object of PLAYER. 
        Returns:
            bool: if current player is the winner returns true. 
        """
        for number in self.Goal_sequence.keys():
            if Rolls.count(number) < self.Goal_sequence[number]:
                return False
        return True     

class Game_C(Game):
    """
    Represents Game C where The sum of values you rolled is equal to the target inorder to win.
    (child of Game)(inherits from game)

    Attributes:
        (all Attributes from Game)
        Goal_sum (int): The target value of the game. 
    """
     
    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players,Goal_sum):
        """ 
        Initializes of Game C.(Inherits from game).

        Args:
            Goal_sum (int): The target value of the game.   
        """
        super().__init__(Player_count,Dice_count,Dice_type,Game_type,Players)

        self.Goal_sum = Goal_sum

    def Check_winner(self,Rolls,Player):
        """
        Checks whether the current rolls sum is equal to target.
        
        Args:
            Rolls (list(int)) : List of current rolls
            Player (PLAYER ) : Current player object of PLAYER 
        Returns:
            Bool: if current player is the winner returns true 
        """
        if sum(Rolls) == self.Goal_sum:
            return True
        return False 

class Game_D(Game):
    """
    Represents Game D Palyer with max score wins after a number of rounds.
    (child of Game)(inherits from game)

    Attributes:
        (all Attributes from Game)
        Rounds (int): Number of rounds for this game. 
    """
     
    def __init__(self,Player_count,Dice_count,Dice_type,Game_type,Players,Rounds):
        """ 
        Initializes of Game D.(Inherits from game).

        Args:
            Rounds (int): Number of rounds for this game. 
        """
        super().__init__(Player_count,Dice_count,Dice_type,Game_type,Players)

        self.Rounds = Rounds

    def game_loop(self):
        """
        Main loop of the game.

        Returns:
            int : ID of the winner.
        """
        current_Round = 1
        Max_id = 0
        Max_Score = 0
        while current_Round < self.Rounds + 1 :
            print("-"*50)
            print(f"ROUND {current_Round}!")
            for id in self.Players:
                Player = self.Players[id]
                print(f"{Player.Name}'s Turn")
                Rolls = self.roll_dice(Player)
                Player.Rolls_History.append(Rolls)
                if sum(Rolls) == self.Dice_count*self.Dice_type:
                    print("Wow! What a roll. You got the max possible score ")
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
    """
    Gives intro about the game
    """
    print(f"{'Dice Game'.center(50,'-')}")
    print("Welcome to Dice Game!")
    print("Rules of the Game:")
    print("Each players playes alternatively.")
    print("You could choose any type of the following Games.")
    print("(Based on the win conditions)")
    print("a) Total score exceeds a particular no.\nb) Who ever rolls  a particular sequence.\nc) Get a particular sum in a roll.\nd) Who could roll the max sum.""")
    print("-"*50)

def Game_start(no_of_players,Players,GAME):
    """
    Creates the game based on users preference and contains replay logic.
    """
    Flag = "y"
    while Flag == 'y':
        id = GAME.game_loop()
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
    Creates the player base.
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
    Gets the inputs from the user to creat the game that they like.(inputs has constrains.)
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
        Reroll_flag = input("Can there be a reroll (y): ").strip().lower()
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
    """
    main part
    """
    Game_intro()
    no_of_players,Players = Game_Players()
    GAME = Game_create(no_of_players,Players)
    Game_start(no_of_players,Players,GAME)
