import sys
sys.path.append('..')
import mysql.connector
import db_config
from nhl_req.requests_handler import Requests_handler
from time import sleep

class NHL_DB:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = db_config.DB_HOSTNAME,
            user = db_config.DB_USERNAME,
            password = db_config.DB_PASSWORD,
            database = db_config.DB_NAME
        )
        self.cursor = self.connection.cursor(buffered=True)
        self.req_handler = Requests_handler()