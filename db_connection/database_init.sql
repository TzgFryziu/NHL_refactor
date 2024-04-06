CREATE DATABASE NHL_TEST;

USE NHL_TEST;

CREATE TABLE Seasons (
    SeasonID INT,
    SeasonYear VARCHAR(10),
    Winner VARCHAR(255),
    TopScoringPlayer VARCHAR(255),
    PRIMARY KEY (SeasonID)
);


CREATE TABLE Teams (
    TeamID INT,
    TeamName VARCHAR(255),
    NameCode VARCHAR(3),
    Manager VARCHAR(255),
    Stadium VARCHAR(255),
    PRIMARY KEY (TeamID)
);

CREATE TABLE TeamsStats (
    TeamID INT,
    SeasonID INT,
    MatchesPlayed INT,
    Wins INT,
    Losses INT,
    Draws INT,
    Points INT,
    ScoresFor INT,
    ScoresAgainst INT,
    FOREIGN KEY (SeasonID) REFERENCES Seasons(SeasonID),
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
);

CREATE TABLE Players (
    PlayerID INT,
    TeamID INT,
    Position VARCHAR(1),
    JerseyNumber INT,
    Height INT,
    Country VARCHAR(255),
    DateOfBirth DATE,
    PRIMARY KEY (PlayerID),
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
);

CREATE TABLE FinishedMatches (
    MatchID INT,
    MatchDate DATE,
    MatchTime TIME,
    HomeTeamID INT,
    AwayTeamID INT,
    HomeScore INT,
    AwayScore INT,
    HomeShots INT,
    AwayShots INT,
    HomeShorhandedGoals INT,
    AwayShorhandedGoals INT,
    HomePowerplayGoals INT,
    AawayPowerplayGoals INT,
    HomeFaceoffsWon INT,
    AwayFaceoffsWon INT,
    HomePenaltyMins INT,
    AwayPenaltyMins INT,
    SeasonID INT,
    PRIMARY KEY (MatchID),
    FOREIGN KEY (HomeTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (AwayTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (SeasonID) REFERENCES Seasons(SeasonID)
);

CREATE TABLE PlayersStats (
    MatchID INT,
    PlayerID INT,
    SecondsPlayed INT,
    Assists INT,
    Goals INT,
    Shots INT,
    Hits INT,
    Accuracy FLOAT(10),
    FOREIGN KEY (MatchID) REFERENCES FinishedMatches(MatchID),
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID)
);

CREATE TABLE UpcomingMatches (
    MatchID INT,
    MatchDate DATE,
    MatchTime TIME,
    HomeTeamID INT,
    AwayTeamID INT,
    SeasonID INT,
    PRIMARY KEY (MatchID),
    FOREIGN KEY (HomeTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (AwayTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (SeasonID) REFERENCES Seasons(SeasonID)
);

CREATE TABLE WinningTeamOdds (
    BetID INT,
    MatchID INT,
    HomeWin FLOAT(10),
    AwayWin FLOAT(10),
    WinningBet INT,
    PRIMARY KEY (BetID),
    FOREIGN KEY (MatchID) REFERENCES UpcomingMatches(MatchID),
    FOREIGN KEY (MatchID) REFERENCES FinishedMatches(MatchID)
);

CREATE TABLE MatchGoalsOdds (
    BetID INT,
    MatchID INT,
    ChoiceGroup FLOAT(5),
    Over_ FLOAT(10),
    Under_ FLOAT(10),
    WinningBet INT,
    PRIMARY KEY (BetID),
    FOREIGN KEY (MatchID) REFERENCES UpcomingMatches(MatchID),
    FOREIGN KEY (MatchID) REFERENCES FinishedMatches(MatchID)
);

