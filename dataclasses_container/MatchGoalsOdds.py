class MatchGoalsOdds:
    def __init__(self,
                 betID: int,
                 matchID: int,
                 choiceGroup: int,
                 over: float,
                 under: float,
                 winningBet: int) -> None:
        self.bet_id = betID
        self.match_id = matchID
        self.choice_group = choiceGroup
        self.over = over
        self.under = under
        self.winning_bet = winningBet