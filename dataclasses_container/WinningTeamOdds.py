class WinningTeamOdds:
    def __init__(
        self, betID: int, matchID: int, homeWin: float, awayWin: float, winningBet: int
    ) -> None:
        self.bet_id = betID
        self.match_id = matchID
        self.home_win = homeWin
        self.away_win = awayWin
        self.winning_bet = winningBet
