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


    def update_finished_matches_id(self, num_pages: int = 1, season_id: int = CURR_SEASON_ID) -> None:
        for i in range(num_pages):
            temp = self.get_response_json_matches_id(get_finished_matches_url, i, season_id)
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
        return UpcomingMatch(match_id,date,home_team,away_team,season_id)


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


    def get_response_json_matches_id(self, url_getter, page_num: int, season_id: int = CURR_SEASON_ID) -> dict | None:   
        sleep(API_TIMEOUT)
        response = requests.get(url_getter(page_num,season_id), headers=API_HEADERS_COMMON)
        if response.status_code != 200:
            return None
        return response.json()
    

