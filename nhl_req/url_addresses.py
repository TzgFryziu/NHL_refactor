def get_match_url(match_id):
    return f"https://api.sofascore.com/api/v1/event/{match_id}"


def get_match_stats_url(match_id):
    return f"https://api.sofascore.com/api/v1/event/{match_id}/lineups"


def get_players_url(player_id):
    return f"https://api.sofascore.com/api/v1/team/{player_id}/players"


def get_teams_url(tournament_id):
    return f"https://api.sofascore.com/api/v1/unique-tournament/234/season/{tournament_id}/standings/total"


def get_odds_url(match_id):
    return f"https://api.sofascore.com/api/v1/event/{match_id}/odds/1/all"

def get_upcoming_matches_url(tournament_id,page_number):
    return f"https://api.sofascore.com/api/v1/unique-tournament/234/season/{tournament_id}/events/last/{page_number}"
