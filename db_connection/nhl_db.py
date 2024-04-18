import sys

sys.path.append("..")
import mysql.connector
from .db_config import *
from nhl_req.requests_handler import Requests_handler
from time import sleep


class NHL_DB:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host=DB_HOSTNAME, user=DB_USERNAME, password=DB_PASSWORD, database=DB_NAME
        )
        self.cursor = self.connection.cursor(buffered=True)
        self.req_handler = Requests_handler()

    def add_all_matches_to_db(self):
        self.add_upcoming_matches()
        self.add_finished_matches()
        self.connection.commit()

    def add_finished_matches(self):
        matches = []
        i = 0
        x = len(self.req_handler.finished_matches_id)

        for match_id in self.req_handler.finished_matches_id:
            self.cursor.execute(
                "SELECT * FROM Matches WHERE matchID = (%s)", (match_id,)
            )
            if self.cursor.fetchone() != None:

                self.cursor.execute(
                    "SELECT homeScore FROM Matches WHERE matchID = (%s)", (match_id,)
                )

                if self.cursor.fetchone() != (None,):
                    print(f"Match {match_id} is already in database!")
                else:
                    print(f"Updating match {match_id}")
                    temp = self.req_handler.fetch_match_data(match_id, "f")
                    self.cursor.execute(
                        """
                    UPDATE matches
                    SET homeScore = %s,
                        awayScore = %s,
                        homeShots = %s,
                        awayShots = %s,
                        homeShorthandedGoals = %s,
                        awayShorthandedGoals = %s,
                        homePowerplayGoals = %s,
                        awayPowerplayGoals = %s,
                        homeFaceoffsWon = %s,
                        awayFaceoffsWon = %s,
                        homePenaltyMins = %s,
                        awayPenaltyMins = %s
                    WHERE matchID = %s                 
                """,
                        (
                            temp.home_score,
                            temp.away_score,
                            temp.home_shots,
                            temp.away_shots,
                            temp.home_shorthanded_goals,
                            temp.away_shorthanded_goals,
                            temp.home_powerplay_goals,
                            temp.away_powerplay_goals,
                            temp.home_faceoffs_won,
                            temp.away_faceoffs_won,
                            temp.home_penalty_mins,
                            temp.away_penalty_mins,
                            match_id,
                        ),
                    )
            else:
                print(f"Adding match {i+1}/{x}")
                temp = self.req_handler.fetch_match_data(match_id, "f")
                matches.append(temp.to_tuple())
            i += 1
        self.cursor.executemany(
            """
            INSERT INTO Matches values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
            matches,
        )

    def add_upcoming_matches(self):
        matches = []
        i = 0
        x = len(self.req_handler.upcoming_matches_id)

        for match_id in self.req_handler.upcoming_matches_id:
            self.cursor.execute(
                "SELECT * FROM Matches WHERE matchID = (%s)", (match_id,)
            )
            if self.cursor.fetchone() != None:
                print(f"Match {match_id} is already in database!")
            else:
                print(f"Adding match {i+1}/{x}")
                temp = self.req_handler.fetch_match_data(match_id, "u")
                matches.append(temp.to_touple())
            i += 1

        self.cursor.executemany(
            """
            INSERT INTO Matches (matchID, matchDate, matchTime, homeTeamID, awayTeamID, seasonID) values (%s,%s,%s,%s,%s,%s)
        """,
            matches,
        )

        self.connection.commit()

    def update_matches(
        self, m_type: str = "f", num_pages: int = 1, season_id: int = CURR_SEASON_ID
    ):
        if m_type == "f":
            self.req_handler.update_finished_matches_id(num_pages, season_id)
            print(self.req_handler.finished_matches_id)
        elif m_type == "u":
            self.req_handler.update_upcoming_matches_id(num_pages)
            print(self.req_handler.upcoming_matches_id)
        else:
            print("Enter f/u")
