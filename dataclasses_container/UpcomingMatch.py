from datetime import datetime


class UpcomingMatch:
    def __init__(
        self,
        matchID: int,
        matchDateTimestamp: int,
        homeTeamID: int,
        awayTeamID: int,
        seasonID: int,
    ):
        self.match_id = matchID
        self.match_date = (
            datetime.fromtimestamp(matchDateTimestamp)
            .strftime("%Y-%m-%d %H:%M:%S")
            .split(" ")[0]
        )
        self.match_time = (
            datetime.fromtimestamp(matchDateTimestamp)
            .strftime("%Y-%m-%d %H:%M:%S")
            .split(" ")[1]
        )
        self.home_team_id = homeTeamID
        self.away_team_id = awayTeamID
        self.season_id = seasonID

    def to_touple(self):
        return (
            self.match_id,
            self.match_date,
            self.match_time,
            self.home_team_id,
            self.away_team_id,
            self.season_id,
        )
