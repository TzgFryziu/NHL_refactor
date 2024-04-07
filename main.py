from nhl_req.requests_handler import Requests_handler

rq = Requests_handler()
rq.update_finished_matches_id(3)
print(rq.finished_matches_id)

