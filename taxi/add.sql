PRAGMA foreign_keys = OFF;

CREATE TABLE Level (
    O_ID INTEGER,
    Level_ID INTEGER,
    PRIMARY KEY (O_ID, Level_ID),
    FOREIGN KEY (O_ID) REFERENCES Opportunity(O_ID),
    FOREIGN KEY (Level_ID) REFERENCES Level_Name(Level_ID)
);