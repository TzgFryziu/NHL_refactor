from db_connection.nhl_db import NHL_DB

database = NHL_DB()

# database.update_seasons()
# database.add_all_teams_to_db()
database.update_matches("u", 2)
# for match in database.querry("SELECT * FROM Matches"):
#     database.update_odds(match[0])


