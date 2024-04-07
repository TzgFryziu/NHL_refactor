class TeamStats:
    def __init__(self,
                 teamID: int,
                 seasonID: int,
                 matchesPlayed: int,
                 wins: int,
                 losses: int,
                 draws: int,
                 points: int,
                 scoresFor: int,
                 scoresAgainst: int) -> None:
        self.team_id = teamID
        self.season_id = seasonID
        self.matches_played = matchesPlayed
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.points = points
        self.scores_for = scoresFor
        self.scores_against = scoresAgainst