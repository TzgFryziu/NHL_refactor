from db_connection.nhl_db import NHL_DB
from nhl_req.requests_handler import Requests_handler

# database = NHL_DB()

# database.update_matches("f", 1)
# database.add_all_matches_to_db()
rq_test = Requests_handler()
rq_test.update_seasons()
