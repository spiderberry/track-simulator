DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS Athletes;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    athlete_id INTEGER,
    FOREIGN KEY (athlete_id) REFERENCES Athletes(id)
);

CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user(id)
);

CREATE TABLE Athletes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    age INTEGER NOT NULL CHECK (age >= 16),
    acceleration TINYINT NOT NULL CHECK (acceleration >= 0 AND acceleration <= 100),
    endurance TINYINT NOT NULL CHECK (endurance >= 0 AND endurance <= 100),
    form TINYINT NOT NULL CHECK (form >= 0 AND form <= 100),
    mental TINYINT NOT NULL CHECK (mental >= 0 AND mental <= 100),
    speed TINYINT NOT NULL CHECK (speed >= 0 AND speed <= 100),
    stamina TINYINT NOT NULL DEFAULT 100 CHECK (stamina >= 0 AND stamina <= 100),
    start TINYINT NOT NULL CHECK (start >= 0 AND start <= 100),
    place TINYINT CHECK (place >= 1 and place <= 8),
    last_race_time REAL,
    last_race_type VARCHAR(30),
    fastest_100m REAL,
    fastest_200m REAL,
    races_ran INTEGER DEFAULT 0,
    overall INTEGER GENERATED ALWAYS AS (CAST ( ( ( (overall_100m + overall_200m + overall_400m) / 3.0) ) AS INTEGER) ) STORED,
    overall_100m INTEGER GENERATED ALWAYS AS (CAST ( (1.5 * acceleration + 1.5 * speed + 1.25 * start + form + 0.75 * endurance + 0.4 * stamina + 0.1 * mental) * 100 / (1.5 * 100 + 1.5 * 100 + 1.25 * 100 + 100 + 0.75 * 100 + 0.4 * 100 + 0.1 * 100) AS INTEGER) ) STORED,
    overall_200m INTEGER GENERATED ALWAYS AS (CAST ( (1.5 * acceleration + 2 * speed + 0.3 * start + form + 1.3 * endurance + 0.7 * stamina + 0.15 * mental) * 100 / (1.5 * 100 + 2 * 100 + 0.3 * 100 + 100 + 1.3 * 100 + 0.7 * 100 + 0.15 * 100) AS INTEGER) ) STORED,
    overall_400m INTEGER GENERATED ALWAYS AS (CAST ( (0.8 * acceleration + 1.1 * speed + 0.2 * start + 1.3 * form + 2.5 * endurance + 0.7 * stamina + 0.4 * mental) * 100 / (0.8 * 100 + 1.1 * 100 + 0.2 * 100 + 1.3 * 100 + 2.5 * 100 + 0.7 * 100 + 0.4 * 100) AS INTEGER) ) STORED
);