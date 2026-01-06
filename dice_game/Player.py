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