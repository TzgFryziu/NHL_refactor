from datetime import datetime


class Finished_match:
    def __init__(
        self,
        matchID: int,
        matchDateTimestamp: int,
        homeTeamID: int,
        awayTeamID: int,
        homeScore: int,
        awayScore: int,
        homeShots: int,
        awayShots: int,
        homeShorthandedGoals: int,
        awayShorthandedGoals: int,
        homePowerplayGoals: int,
        awayPowerplayGoals: int,
        homeFacoffsWon: int,
        awayFaceoffsWon: int,
        homePenaltyMins: int,
        awayPenaltyMins: int,
        seasonID: int,
    ) -> None:
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
        self.home_score = homeScore
        self.away_score = awayScore
        self.home_shots = homeShots
        self.away_shots = awayShots
        self.home_shorthanded_goals = homeShorthandedGoals
        self.away_shorthanded_goals = awayShorthandedGoals
        self.home_powerplay_goals = homePowerplayGoals
        self.away_powerplay_goals = awayPowerplayGoals
        self.home_faceoffs_won = homeFacoffsWon
        self.away_faceoffs_won = awayFaceoffsWon
        self.home_penalty_mins = homePenaltyMins
        self.away_penalty_mins = awayPenaltyMins
        self.season_id = seasonID

    def to_tuple(self):
        return (
            self.match_id,
            self.match_date,
            self.match_time,
            self.home_team_id,
            self.away_team_id,
            self.home_score,
            self.away_score,
            self.home_shots,
            self.away_shots,
            self.home_shorthanded_goals,
            self.away_shorthanded_goals,
            self.home_powerplay_goals,
            self.away_powerplay_goals,
            self.home_faceoffs_won,
            self.away_faceoffs_won,
            self.home_penalty_mins,
            self.away_penalty_mins,
            self.season_id,
        )
