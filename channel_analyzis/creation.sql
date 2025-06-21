-- Table for Educational Levels
CREATE TABLE educational_level (
    o_id INTEGER NOT NULL,
    educational_level_id INTEGER NOT NULL,
    FOREIGN KEY (o_id) REFERENCES opportunities(o_id),
    FOREIGN KEY (educational_level_id) REFERENCES educational_level_names(educational_level_id),
);
CREATE TABLE educational_level_names (
    educational_level_id INTEGER PRIMARY KEY,
    educational_level_name TEXT NOT NULL
);

-- Table for Fields
CREATE TABLE field (
    o_id INTEGER NOT NULL,
    field_id INTEGER NOT NULL,
    FOREIGN KEY (o_id) REFERENCES opportunities(o_id),
    FOREIGN KEY (field_id) REFERENCES field_names(field_id)
);
CREATE TABLE field_names (
    field_id INTEGER PRIMARY KEY,
    field_name TEXT NOT NULL
);

-- Table for Outcomes
CREATE TABLE outcome (
    o_id INTEGER NOT NULL,
    outcome_id INTEGER NOT NULL,
    FOREIGN KEY (o_id) REFERENCES opportunities(o_id),
    FOREIGN KEY (outcome_id) REFERENCES outcome_names(outcome_id)
);
CREATE TABLE outcome_names (
    outcome_id INTEGER PRIMARY KEY,
    outcome_name TEXT NOT NULL
);

-- Table for Audience
CREATE TABLE audience (
    o_id INTEGER NOT NULL,
    audience_id INTEGER NOT NULL,
    FOREIGN KEY (o_id) REFERENCES opportunities(o_id),
    FOREIGN KEY (audience_id) REFERENCES audience_names(audience_id)
);
CREATE TABLE audience_names (
    audience_id INTEGER PRIMARY KEY,
    audience_name TEXT NOT NULL
);

CREATE TABLE organizer (
    o_id INTEGER NOT NULL,
    organizer_id INTEGER NOT NULL,
    FOREIGN KEY (o_id) REFERENCES opportunities(o_id),
    FOREIGN KEY (organizer_id) REFERENCES organizer_names(organizer_id)
);
CREATE TABLE organizer_names (
    organizer_id INTEGER PRIMARY KEY,
    organizer_name TEXT NOT NULL
);

-- Table for Geography
CREATE TABLE geography (
    o_id INTEGER NOT NULL,
    geography_id INTEGER NOT NULL,
    FOREIGN KEY (o_id) REFERENCES opportunities(o_id),
    FOREIGN KEY (geography_id) REFERENCES geography_names(geography_id)
);
CREATE TABLE geography_names (
    geography_id INTEGER PRIMARY KEY,
    geography_name TEXT NOT NULL
);

-- Table for Location
CREATE TABLE location (
    o_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    FOREIGN KEY (o_id) REFERENCES opportunities(o_id),
    FOREIGN KEY (location_id) REFERENCES location_names(location_id)
);
CREATE TABLE location_names (
    location_id INTEGER PRIMARY KEY,
    location_name TEXT NOT NULL
);

-- Table for Language
CREATE TABLE language (
    o_id INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    FOREIGN KEY (o_id) REFERENCES opportunities(o_id),
    FOREIGN KEY (language_id) REFERENCES language_names(language_id)
);
CREATE TABLE language_names (
    language_id INTEGER PRIMARY KEY,
    language_name TEXT NOT NULL
);

-- Table for Tag
CREATE TABLE tag (
    o_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY (o_id) REFERENCES opportunities(o_id),
    FOREIGN KEY (tag_id) REFERENCES tag_names(tag_id)
);
CREATE TABLE tag_names (
    tag_id INTEGER PRIMARY KEY,
    tag_name TEXT NOT NULL
);