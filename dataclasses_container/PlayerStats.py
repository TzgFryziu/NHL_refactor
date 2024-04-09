class PlayerStats:
    def __init__(self,
                 matchID: int,
                 playerID: int,
                 secondsPlayed: int,
                 assists: int,
                 goals: int,
                 shots: int,
                 hits: int
                 ) -> None:
        self.match_id = matchID
        self.player_id = playerID
        self.seconds_played = secondsPlayed
        self.assists = assists
        self.goals = goals
        self.shots = shots
        self.hits = hits
        self.accuracy = goals/shots