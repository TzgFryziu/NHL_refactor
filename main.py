from db_connection.nhl_db import NHL_DB

database = NHL_DB()

database.update_matches("f",1)
database.add_all_matches_to_db()
