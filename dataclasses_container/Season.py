class Season:
    def __init__(
        self, seasonID: int, seasonYear: str, winner: str, topScoringPlayer: int
    ) -> None:
        self.season_id = seasonID
        self.season_year = seasonYear
        self.winner = winner
        self.top_scoring_player = topScoringPlayer
