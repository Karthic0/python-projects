from dice_game_main import Game 
from dice_game_main import Game_A as a
from dice_game_main import Game_B as b
from dice_game_main import Game_C as c
from dice_game_main import Game_D as d
from dice_game_main import PLAYER as player
import builtins  

builtins.input =lambda _:'n'

def test_player():
    """
    Test the player class initialization and reset method.
    """
    p = player("karthic")
    assert p.Name == "karthic"
    assert p.Score == 0
    assert p.Rolls_History == []
    assert p.Wins == 0

    p.Score = 10
    p.Rolls_History = [[1,2,6,1]]
    p.Reset()
    assert p.Name == "karthic"
    assert p.Score == 0
    assert p.Rolls_History == []
    assert p.Wins == 0

def test_game():
    """
    Test the Game class initialization and Roll_dice method along with reroll condition.
    """
    p = player("karthic")
    game = Game(1,3,6,None,{1: p})

    game.Reroll_flag = False
    rolls = game.roll_dice(p)
    assert len(rolls) == 3
    for roll in rolls:
        assert 1 <= roll <= 6
    
    game.Reroll_flag = True
    rolls = game.roll_dice(p)
    assert len(rolls) == 3
    for roll in rolls:
        assert 1 <= roll <= 6

def test_a():
    """
    Test the Game_A class  (Particular score) initialization , win condition and score reset condition.
    """
    p = player("karthic")
    win_score = 10
    game = a(1,3,6,None,{1: p},win_score,5)

    p.Score = 7
    rolls = [2,3,5]
    win = game.Check_winner(rolls,p)
    assert p.Score == 0
    assert win == False

    p.Score = 10
    win = game.Check_winner([],p)
    assert win == True

def test_b():
    """
    Test the Game_B class (sequence) initialization and win condition .
    """
    p = player("karthic")
    Goal_sequence = [2,2,5]
    game = b(1,5,6,None,{1: p},Goal_sequence)

    rolls = [2,2,4,6,6]
    win = game.Check_winner(rolls,p)
    assert win == False
    rolls = [2,2,5,5,6]
    win = game.Check_winner(rolls,p)
    assert win == True

def test_c():
    """
    Test the Game_C class (Target sum) initialization and win condition .
    """
    p = player("karthic")
    Target_sum = 10
    game = c(1,5,6,None,{1: p},Target_sum)

    rolls = [2,2,2,2,1]
    win = game.Check_winner(rolls,p)
    assert win == False
    rolls = [2,2,2,2,2]
    win = game.Check_winner(rolls,p)
    assert win == True

def test_d():
    """
    Test the Game_C class (Target sum) initialization and game loop.
    """
    p1 = player("karthic")
    p2 = player("kavin")
    No_of_rounds = 10
    game = d(2,2,2,None,{0: p1,1:p2},No_of_rounds)
    winner = game.game_loop()
    assert winner in [0, 1]

if __name__ == "__main__":
    test_player()
    test_game()
    test_a()
    test_b()
    test_c()
    test_d()