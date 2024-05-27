CREATE DATABASE NHL_TEST;

USE NHL_TEST;

CREATE TABLE Seasons (
    seasonID INT,
    seasonYear VARCHAR(10),
    winner VARCHAR(255),
    topScoringPlayer VARCHAR(255),
    PRIMARY KEY (seasonID)
);


CREATE TABLE Teams (
    teamID INT,
    teamName VARCHAR(255),
    nameCode VARCHAR(3),
    manager VARCHAR(255),
    stadium VARCHAR(255),
    PRIMARY KEY (teamID)
);

CREATE TABLE TeamsStats (
    teamID INT,
    seasonID INT,
    matchesPlayed INT,
    wins INT,
    losses INT,
    draws INT,
    points INT,
    scoresFor INT,
    scoresAgainst INT,
    FOREIGN KEY (seasonID) REFERENCES seasons(seasonID),
    FOREIGN KEY (teamID) REFERENCES teams(teamID)
);

CREATE TABLE Players (
    playerID INT,
    teamID INT,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    position VARCHAR(1),
    jerseyNumber INT,
    height INT,
    country VARCHAR(255),
    dateOfBirth DATE,
    PRIMARY KEY (playerID),
    FOREIGN KEY (teamID) REFERENCES teams(teamID)
);

CREATE TABLE Matches (
    matchID INT,
    matchDate DATE,
    matchTime TIME,
    homeTeamID INT,
    awayTeamID INT,
    homeScore INT,
    awayScore INT,
    homeShots INT,
    awayShots INT,
    homeShorhandedGoals INT,
    awayShorhandedGoals INT,
    homePowerplayGoals INT,
    awayPowerplayGoals INT,
    homeFaceoffsWon INT,
    awayFaceoffsWon INT,
    homePenaltyMins INT,
    awayPenaltyMins INT,
    seasonID INT,
    PRIMARY KEY (matchID),
    FOREIGN KEY (homeTeamID) REFERENCES teams(teamID),
    FOREIGN KEY (awayTeamID) REFERENCES teams(teamID),
    FOREIGN KEY (seasonID) REFERENCES seasons(seasonID)
);

CREATE TABLE PlayersStats (
    matchID INT,
    playerID INT,
    secondsPlayed INT,
    assists INT,
    goals INT,
    shots INT,
    hits INT,
    accuracy FLOAT(10),
    FOREIGN KEY (matchID) REFERENCES Matches(matchID),
    FOREIGN KEY (playerID) REFERENCES players(playerID)
);



CREATE TABLE WinningTeamOdds (
    betID INT,
    matchID INT,
    homeWin FLOAT(10),
    awayWin FLOAT(10),
    winningBet INT,
    PRIMARY KEY (betID),
    FOREIGN KEY (matchID) REFERENCES Matches(matchID)

);

CREATE TABLE MatchGoalsOdds (
    betID INT,
    matchID INT,
    choiceGroup FLOAT(5),
    over_ FLOAT(10),
    under_ FLOAT(10),
    winningBet INT,
    PRIMARY KEY (betID),
    FOREIGN KEY (matchID) REFERENCES Matches(matchID)

);

