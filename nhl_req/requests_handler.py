from .req_config import *
from time import sleep
import requests
from .url_addresses import *
from dataclasses_container.Finished_match import Finished_match
from dataclasses_container.MatchGoalsOdds import MatchGoalsOdds
from dataclasses_container.Player import Player
from dataclasses_container.PlayerStats import PlayerStats
from dataclasses_container.Season import Season
from dataclasses_container.Team_stats import TeamStats
from dataclasses_container.Team import Team
from dataclasses_container.UpcomingMatch import UpcomingMatch
from dataclasses_container.WinningTeamOdds import WinningTeamOdds


class Requests_handler:
    def __init__(self) -> None:
        self.upcoming_matches_id = []
        self.finished_matches_id = []

    def update_seasons(self) -> list[tuple[int, str, int, str]]:
        result = []
        i =0
        x = len(SEASONS)
        for season in SEASONS.keys():
            i += 1
            print(f"Fetching season {i}/{x}")
            top_player_json = self.get_response_json(get_top_players, season)
            if top_player_json:
                top_player = top_player_json["topPlayers"]["points"][0]["player"][
                    "name"
                ]
            else:
                top_player = None

            winner_json = self.get_response_json(get_cuptrees, season)
            if winner_json:
                try:
                    match_result = winner_json["cupTrees"][0]["rounds"][-1]["blocks"][
                        0
                    ]["result"]
                except KeyError:
                    match_result = None

                if match_result == "away won":
                    winner = winner_json["cupTrees"][0]["rounds"][-1]["blocks"][0][
                        "participants"
                    ][1]["team"]["id"]
                else:
                    try:
                        winner = winner_json["cupTrees"][0]["rounds"][-1]["blocks"][0][
                            "participants"
                        ][0]["team"]["id"]
                    except IndexError:
                        winner = None
            else:
                winner = None
            temp = (season, SEASONS[season], winner, top_player)
            result.append(temp)
            
        return result

    def fetch_teams_data(self, season: int) -> list[tuple[int, str, str]]:
        result = []
        teams_json = self.get_response_json(get_teams_url, season)
        teams = teams_json["standings"][6]["rows"]

        for team in teams:
            team_id = team["team"]["id"]
            team_name = team["team"]["name"]
            team_namecode = team["team"]["nameCode"]
            temp = (team_id, team_name, team_namecode)
            result.append(temp)
        return result
    
    def fetch_teams_stats(self, season: int) -> list[tuple[int,int,int,int,int,int,int,int,int]]:
        result = []
        teams_json = self.get_response_json(get_teams_url, season)
        teams = teams_json["standings"][6]["rows"]

        for team in teams:
            team_id = team["team"]["id"]
            season_id = season
            wins = team["wins"]
            draws = team["draws"]
            losses = team["losses"]
            matches_played = wins + draws + losses
            poins = team["points"]
            scoresFor = team["scoresFor"]
            scoresAgainst = team["scoresAgainst"]
            temp = (team_id, season_id, matches_played, wins,losses, draws,  poins, scoresFor, scoresAgainst)
            
            result.append(temp)
        return result

    def update_finished_matches_id(
        self, num_pages: int = 1, season_id: int = CURR_SEASON_ID
    ) -> None:
        for i in range(num_pages):
            temp = self.get_response_json_matches_id(
                get_finished_matches_url, i, season_id
            )
            if temp:
                self.finished_matches_id.extend(event["id"] for event in temp["events"])
            else:
                break

    def fetch_match_data(self, match_id: int, m_type: str):
        match_json = self.get_response_json(get_match_url, match_id)
        date = match_json["event"]["startTimestamp"]
        home_team = match_json["event"]["homeTeam"]["id"]
        away_team = match_json["event"]["awayTeam"]["id"]
        season_id = match_json["event"]["season"]["id"]

        if m_type == "f":
            stats_json = self.get_response_json(get_match_stats_url, match_id)
            home_score = match_json["event"]["homeScore"]["current"]
            away_score = match_json["event"]["awayScore"]["current"]
            home_shots = stats_json["statistics"][0]["groups"][0]["statisticsItems"][0][
                "home"
            ]
            away_shots = stats_json["statistics"][0]["groups"][0]["statisticsItems"][0][
                "away"
            ]
            home_shorthanded_goals = stats_json["statistics"][0]["groups"][0][
                "statisticsItems"
            ][2]["home"]
            away_shorthanded_goals = stats_json["statistics"][0]["groups"][0][
                "statisticsItems"
            ][2]["away"]
            home_powerplay_goals = stats_json["statistics"][0]["groups"][0][
                "statisticsItems"
            ][1]["home"]
            away_powerplay_goals = stats_json["statistics"][0]["groups"][0][
                "statisticsItems"
            ][1]["away"]
            home_faceoffs_won = stats_json["statistics"][0]["groups"][0][
                "statisticsItems"
            ][3]["home"].split(" ")[1][1:-2]
            away_faceoffs_won = stats_json["statistics"][0]["groups"][0][
                "statisticsItems"
            ][3]["away"].split(" ")[1][1:-2]
            home_penalty_mins = stats_json["statistics"][0]["groups"][0][
                "statisticsItems"
            ][8]["home"]
            away_penalty_mins = stats_json["statistics"][0]["groups"][0][
                "statisticsItems"
            ][8]["away"]

            return Finished_match(
                match_id,
                date,
                home_team,
                away_team,
                home_score,
                away_score,
                home_shots,
                away_shots,
                home_shorthanded_goals,
                away_shorthanded_goals,
                home_powerplay_goals,
                away_powerplay_goals,
                home_faceoffs_won,
                away_faceoffs_won,
                home_penalty_mins,
                away_penalty_mins,
                season_id,
            )

        return UpcomingMatch(match_id, date, home_team, away_team, season_id)

    def update_upcoming_matches_id(self, num_pages: int = 1) -> None:
        for i in range(num_pages):
            temp = self.get_response_json_matches_id(get_upcoming_matches_url, i)
            if temp:
                self.upcoming_matches_id.extend(event["id"] for event in temp["events"])
            else:
                break

    def get_response_json(self, url_getter, id: int) -> dict | None:
        sleep(API_TIMEOUT)
        response = requests.get(url_getter(id), headers=API_HEADERS_COMMON)
        if response.status_code != 200:
            return None
        return response.json()

    def get_response_json_matches_id(
        self, url_getter, page_num: int, season_id: int = CURR_SEASON_ID
    ) -> dict | None:
        sleep(API_TIMEOUT)
        response = requests.get(
            url_getter(page_num, season_id), headers=API_HEADERS_COMMON
        )
        if response.status_code != 200:
            return None
        return response.json()

    def fetch_odds(self,match_id: int) -> tuple[tuple[int,int,float,float,int],tuple[int,int,float,float,float,int]]:
        odds_json = self.get_response_json(get_odds_url, match_id)
        home_odds = (float(odds_json["markets"][0]["choices"][0]["initialFractionalValue"].split("/")[0])/float(odds_json["markets"][0]["choices"][0]["initialFractionalValue"].split("/")[1]))+1
        away_odds = (float(odds_json["markets"][0]["choices"][1]["initialFractionalValue"].split("/")[0])/float(odds_json["markets"][0]["choices"][1]["initialFractionalValue"].split("/")[1]))+1
        winning_bet_id = odds_json["markets"][0]["id"]
        if odds_json["markets"][0]["choices"][0]["winning"] == True:
            winning = 1
        else:
            winning = 2

        goals_bet_id = odds_json["markets"][-1]["id"]
        choice_group = float(odds_json["markets"][-1]["choiceGroup"])
        over_odds = (float(odds_json["markets"][-1]["choices"][0]["initialFractionalValue"].split("/")[0])/float(odds_json["markets"][-1]["choices"][0]["initialFractionalValue"].split("/")[1]))+1
        under_odds = (float(odds_json["markets"][-1]["choices"][1]["initialFractionalValue"].split("/")[0])/float(odds_json["markets"][-1]["choices"][1]["initialFractionalValue"].split("/")[1]))+1
        if odds_json["markets"][-1]["choices"][0]["winning"] == True:
            winning_g = 1
        else:
            winning_g = 2

        return [(winning_bet_id,match_id,home_odds,away_odds,winning),
                (goals_bet_id,match_id,choice_group,over_odds,under_odds,winning_g)]