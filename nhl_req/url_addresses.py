def get_match_url(match_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/event/{match_id}"


def get_players_stats_url(match_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/event/{match_id}/lineups"


def get_match_stats_url(match_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/event/{match_id}/statistics"


def get_players_url(player_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/team/{player_id}"


def get_teams_url(season_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/unique-tournament/234/season/{season_id}/standings/total"


def get_odds_url(match_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/event/{match_id}/odds/1/all"


def get_finished_matches_url(page_number: int, season_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/unique-tournament/234/season/{season_id}/events/last/{page_number}"


def get_upcoming_matches_url(page_number: int, season_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/unique-tournament/234/season/{season_id}/events/next/{page_number}"


def get_top_players(season_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/unique-tournament/234/season/{season_id}/top-players/regularSeason"


def get_cuptrees(season_id: int) -> str:
    return f"https://api.sofascore.com/api/v1/unique-tournament/234/season/{season_id}/cuptrees"
