
--CREATING THE DARABASE

CREATE TABLE Opportunity (
    O_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    O_Description TEXT,
    O_Title TEXT NOT NULL,
    O_Source INTEGER,
    O_Link TEXT,
    O_Deadline DATE,
    O_Start_Date DATE,
    O_Duration INTEGER,  -- Duration in days
    O_Max_Age INTEGER,
    O_Min_Age INTEGER,
    O_Date_Added DATE,
    O_Last_Updated DATE,
    
    FOREIGN KEY (O_Source) REFERENCES Source_Name(Source_ID)
);

CREATE TABLE Source_Name (
    Source_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Source_Name TEXT NOT NULL
);

CREATE TABLE Level_Name (
    Level_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Level_Name TEXT NOT NULL
);
CREATE TABLE Level (
    O_ID INTEGER,
    Level_ID INTEGER,
    PRIMARY KEY (O_ID, Level_ID),
    FOREIGN KEY (O_ID) REFERENCES Opportunity(O_ID),
    FOREIGN KEY (Level_ID) REFERENCES Level_Name(Level_ID)
);

CREATE TABLE Type_Name (
    Type_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Type_Name TEXT NOT NULL
);CREATE TABLE Type_ (
    O_ID INTEGER,
    Type_ID INTEGER,
    PRIMARY KEY (O_ID, Type_ID),
    FOREIGN KEY (O_ID) REFERENCES Opportunity(O_ID),
    FOREIGN KEY (Type_ID) REFERENCES Type_Name(Type_ID)
);

CREATE TABLE Field_Name (
    Field_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Field_Name TEXT NOT NULL
);CREATE TABLE Field (
    O_ID INTEGER,
    Field_ID INTEGER,
    PRIMARY KEY (O_ID, Field_ID),
    FOREIGN KEY (O_ID) REFERENCES Opportunity(O_ID),
    FOREIGN KEY (Field_ID) REFERENCES Field_Name(Field_ID)
);

CREATE TABLE Audience_Name (
    Audience_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Audience_Name TEXT NOT NULL
);CREATE TABLE Audience (
    O_ID INTEGER,
    Audience_ID INTEGER,
    PRIMARY KEY (O_ID, Audience_ID),
    FOREIGN KEY (O_ID) REFERENCES Opportunity(O_ID),
    FOREIGN KEY (Audience_ID) REFERENCES Audience_Name(Audience_ID)
);

CREATE TABLE Educational_Level_Name (
    Educational_Level_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Educational_Level_Name TEXT NOT NULL
);CREATE TABLE Educational_Level (
    O_ID INTEGER,
    Educational_Level_ID INTEGER,
    PRIMARY KEY (O_ID, Educational_Level_ID),
    FOREIGN KEY (O_ID) REFERENCES Opportunity(O_ID),
    FOREIGN KEY (Educational_Level_ID) REFERENCES Educational_Level_Name(Educational_Level_ID)
);

CREATE TABLE Geography_Name (
    Geography_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Geography_Name TEXT NOT NULL
);
CREATE TABLE Geography (
    O_ID INTEGER,
    Geography_ID INTEGER,
    PRIMARY KEY (O_ID, Geography_ID),
    FOREIGN KEY (O_ID) REFERENCES Opportunity(O_ID),
    FOREIGN KEY (Geography_ID) REFERENCES Geography_Name(Geography_ID)
);

CREATE TABLE Outcome_Name (
    Outcome_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Outcome_Name TEXT NOT NULL
);
CREATE TABLE Outcome (
    O_ID INTEGER,
    Outcome_ID INTEGER,
    PRIMARY KEY (O_ID, Outcome_ID),
    FOREIGN KEY (O_ID) REFERENCES Opportunity(O_ID),
    FOREIGN KEY (Outcome_ID) REFERENCES Outcome_Name(Outcome_ID)
);

CREATE TABLE Language_Name (
    Language_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Language_Name TEXT NOT NULL
);
CREATE TABLE Language (
    O_ID INTEGER,
    Language_ID INTEGER,
    PRIMARY KEY (O_ID, Language_ID),
    FOREIGN KEY (O_ID) REFERENCES Opportunity(O_ID),
    FOREIGN KEY (Language_ID) REFERENCES Language_Name(Language_ID)
);



