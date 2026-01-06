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