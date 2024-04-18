from datetime import datetime


class Player:
    def __init__(
        self,
        playerID: int,
        teamID: int,
        name: str,
        position: str,
        jerseyNumber: int,
        height: int,
        country: str,
        dateOfBirthTimestamp: int,
    ) -> None:
        self.player_id = playerID
        self.team_id = teamID
        self.first_name, self.last_name = name.split(" ")
        self.position = position
        self.jersey_number = jerseyNumber
        self.height = height
        self.country = country
        self.date_of_birth = (
            datetime.fromtimestamp(dateOfBirthTimestamp)
            .strftime("%Y-%m-%d %H:%M:%S")
            .split(" ")[0]
        )
