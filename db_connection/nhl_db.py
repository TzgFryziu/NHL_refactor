import sys
sys.path.append('..')
import mysql.connector
from .db_config import *
from nhl_req.requests_handler import Requests_handler
from time import sleep




class NHL_DB:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = DB_HOSTNAME,
            user = DB_USERNAME,
            password = DB_PASSWORD,
            database = DB_NAME
        )
        self.cursor = self.connection.cursor(buffered=True)
        self.req_handler = Requests_handler()

    def update_matches(self,
                       m_type: str = "f",
                       num_pages: int = 1,
                       season_id: int = CURR_SEASON_ID):
        if m_type == "f":
            self.req_handler.update_finished_matches_id(num_pages,season_id)
            print(self.req_handler.finished_matches_id)
        elif m_type == "u":
            self.req_handler.update_upcoming_matches_id(num_pages)
            print(self.req_handler.upcoming_matches_id)
        else:
            print("Enter f/u")
        
        