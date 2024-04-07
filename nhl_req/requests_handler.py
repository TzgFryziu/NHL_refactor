from .req_config import *
from time import sleep
import requests
from .url_addresses import *

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


    def get_response_json_matches_id(self, url_getter, page_num: int, season_id: int) -> dict | None:   
        sleep(API_TIMEOUT)
        response = requests.get(url_getter(page_num,season_id), headers=API_HEADERS_COMMON)
        if response.status_code != 200:
            return None
        return response.json()
