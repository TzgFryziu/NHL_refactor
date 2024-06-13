-- Kwerenda, która zwraca zwycięzców sezonów oraz najlepiej punktujących graczy:
SELECT 
    S.seasonYear AS Season,
    S.winner AS Winner,
    S.topScoringPlayer AS TopScoringPlayer
FROM 
    Seasons S;

-- Kwerenda, która wyświetla sezon, nazwę drużyny oraz statystyki drużyny
SELECT 
    S.seasonYear AS Season,
    T.teamName AS Team,
    TS.matchesPlayed AS MatchesPlayed,
    TS.wins AS Wins,
    TS.losses AS Losses,
    TS.draws AS Draws,
    TS.points AS Points,
    TS.scoresFor AS ScoresFor,
    TS.scoresAgainst AS ScoresAgainst
FROM 
    Teams T
JOIN 
    TeamsStats TS ON T.teamID = TS.teamID
JOIN 
    Seasons S ON TS.seasonID = S.seasonID;


-- Kwerenda, która zwraca kursy dla wszystkich meczów wraz z nazwami drużyn
SELECT 
    M.matchID,
    S.seasonYear AS Season,
    HT.teamName AS HomeTeam,
    AT.teamName AS AwayTeam,
    W.homeWin,
    W.awayWin,
    W.winningBet
FROM 
    WinningTeamOdds W
JOIN 
    Matches M ON W.matchID = M.matchID
JOIN 
    Teams HT ON M.homeTeamID = HT.teamID
JOIN 
    Teams AT ON M.awayTeamID = AT.teamID
JOIN 
    Seasons S ON M.seasonID = S.seasonID;

-- Kwerenda, która zwraca zakłady na ilość goli dla wszystkich meczów:
SELECT 
    M.matchID,
    S.seasonYear AS Season,
    HT.teamName AS HomeTeam,
    AT.teamName AS AwayTeam,
    G.choiceGroup,
    G.over_,
    G.under_,
    G.winningBet
FROM 
    MatchGoalsOdds G
JOIN 
    Matches M ON G.matchID = M.matchID
JOIN 
    Teams HT ON M.homeTeamID = HT.teamID
JOIN 
    Teams AT ON M.awayTeamID = AT.teamID
JOIN 
    Seasons S ON M.seasonID = S.seasonID;

