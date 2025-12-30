from random import randint as Generator

def Display_Score(Players,VALUE): # displays the scoreboard
    max_player_length = max([len(x) for x in Players.keys()] + [7]) 
    values_length = max(len(str(VALUE)),6)

    print((max_player_length + values_length + 7) * "-")
    print(f"| {'SCOREBOARD':^{max_player_length + values_length + 3}} |")
    print((max_player_length + values_length + 7) * "-")
    print(f"| {'players':^{max_player_length}} | {'Scores':^{values_length}} |")
    print((max_player_length + values_length + 7) * "-")
    
    for player in Players.keys():
        print(f"| {player:^{max_player_length}} | {str(Players[player]['Score']):^{values_length }} |")
    print((max_player_length + values_length + 7) * "-")

def Roll_Dice(DICES,SIDES): # simple rolling of n dice
    total = 0
    for dice in range(DICES):
        Value = Generator(1,SIDES)
        print(f"     Dice {dice + 1} value ; {Value}")
        total += Value
    return total

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
