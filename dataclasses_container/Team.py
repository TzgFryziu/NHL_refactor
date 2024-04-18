class Team:
    def __init__(
        self, teamID: int, teamName: str, nameCode: str, manager: str, stadium: str
    ) -> None:
        self.team_id = teamID
        self.team_name = teamName
        self.name_code = nameCode
        self.manager = manager
        self.stadium = stadium
